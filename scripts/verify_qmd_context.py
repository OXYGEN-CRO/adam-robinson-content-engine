#!/usr/bin/env python3
"""Audit this checkout's QMD text/vector coverage without changing any index.

Uses the wrapper's selected index and the installed QMD runtime's own path,
title, FTS normalization, model-resolution and fingerprint functions. SQLite
is opened with readonly/fileMustExist plus query_only, inside one read snapshot.
No createStore, update, embed, doctor, migrations or configuration writes run.

Required scope: the combined 914 LinkedIn records, selected 100 YouTube
transcripts, every Markdown page in the six context directories, index/log,
and supplemental archived raw Markdown. Vendor/build/hidden/ignored files
are excluded from recursive discovery; selected sources cannot be excluded.

Exit 0 means all required documents passed, 1 means coverage/isolation failed,
and 2 means the auditor could not complete. The JSON report is always replaced
atomically; the QMD database and configuration are never written.
"""

import argparse
import collections
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOTS = ('identity', 'audience', 'strategy', 'voice', 'brand', 'inspiration')
EXCLUDED_PARTS = {'node_modules', 'vendor', 'dist', 'build', 'output', '__pycache__'}
LI_MANIFEST = 'raw/sources/2026-09-08-linkedin-rb2b/posts.normalized.json'
YT_MANIFEST = 'raw/sources/2026-09-08-youtube/selected-100.json'

# Deliberately use only pure exports from QMD. The CLI's model resolver persists
# defaults, and createStore runs schema/config migrations, so neither is called.
NODE_AUDIT = r'''
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const sha = value => crypto.createHash('sha256').update(value).digest('hex');
const req = createRequire(path.join(input.package_root, 'package.json'));
const store = await import(pathToFileURL(path.join(input.package_root, 'dist/store.js')));
const cfg = await import(pathToFileURL(path.join(input.package_root, 'dist/collections.js')));
const llm = await import(pathToFileURL(path.join(input.package_root, 'dist/llm.js')));
const dbModule = await import(pathToFileURL(path.join(input.package_root, 'dist/db.js')));
const picomatch = req('picomatch');
cfg.setConfigIndexName(input.index_name);
cfg.setConfigSource(); // Matches the wrapper's explicit --index; no disk write.
const config = cfg.loadConfig();
const model = llm.resolveEmbedModel(config.models);
const fingerprint = store.getEmbeddingFingerprint(model);
const configPath = cfg.getConfigPath();
const configHash = fs.existsSync(configPath) ? sha(fs.readFileSync(configPath)) : null;
const Database = req('better-sqlite3');
const db = new Database(input.database_path, { readonly: true, fileMustExist: true });
dbModule.loadSqliteVec(db);
db.pragma('query_only = ON');
db.exec('BEGIN');
const result = { errors: [], documents: [], runtime: {
  model, embedding_fingerprint: fingerprint, config_path: configPath,
  config_sha256: configHash, database_readonly: db.readonly,
  query_only: db.pragma('query_only', { simple: true }),
  chunk_size_tokens: store.CHUNK_SIZE_TOKENS,
  chunk_overlap_tokens: store.CHUNK_OVERLAP_TOKENS,
  implementation_sha256: Object.fromEntries(
    ['dist/store.js', 'dist/llm.js', 'dist/db.js', 'dist/collections.js', 'dist/cli/qmd.js']
    .map(p => [p, sha(fs.readFileSync(path.join(input.package_root, p)))]))
}};
try {
  const schemas = db.prepare(`SELECT name, sql FROM sqlite_master WHERE name IN
    ('documents','content','content_vectors','vectors_vec','documents_fts',
     'store_collections','store_config')`).all();
  result.schema = Object.fromEntries(schemas.map(r => [r.name, r.sql]));
  const required = {
    documents: ['id','collection','path','title','hash','active'],
    content: ['hash','doc'],
    content_vectors: ['hash','seq','pos','model','embed_fingerprint','total_chunks','embedded_at'],
    store_collections: ['name','path','pattern','ignore_patterns','include_by_default'],
    store_config: ['key','value'],
    documents_fts: ['filepath','title','body'],
    vectors_vec: ['hash_seq','embedding']
  };
  for (const [table, columns] of Object.entries(required)) {
    const found = new Set(db.prepare(`PRAGMA table_info(${table})`).all().map(r => r.name));
    for (const column of columns) if (!found.has(column))
      throw new Error(`Unsupported installed schema: ${table}.${column} missing`);
  }
  const dimensionMatch = result.schema.vectors_vec.match(/embedding\s+float\[(\d+)\]/i);
  if (!dimensionMatch) throw new Error('Unsupported vectors_vec embedding schema');
  const dimensions = Number(dimensionMatch[1]);
  result.runtime.vector_dimensions = dimensions;
  result.collections = db.prepare('SELECT * FROM store_collections').all();
  const collection = result.collections.find(c => c.name === 'context');
  const yamlCollection = config.collections?.context;
  if (!collection) throw new Error('Missing context collection in index');
  for (const c of result.collections) {
    if (c.name !== 'context' || fs.realpathSync(c.path) !== input.root)
      result.errors.push(`Unexpected collection or external root: ${c.name}: ${c.path}`);
  }
  if (Object.keys(config.collections || {}).length !== 1 || !yamlCollection ||
      fs.realpathSync(yamlCollection.path) !== input.root)
    result.errors.push('YAML collection configuration is not isolated to this repo/context');
  if (collection.pattern !== '**/*.md' || yamlCollection?.pattern !== '**/*.md')
    result.errors.push('Expected context archive pattern **/*.md in SQLite and YAML');
  if (collection.include_by_default !== 1 || yamlCollection?.includeByDefault === false)
    result.errors.push('Context is excluded from default retrieval');
  const ignores = collection.ignore_patterns ? JSON.parse(collection.ignore_patterns) : [];
  const yamlIgnores = yamlCollection?.ignore || [];
  result.runtime.yaml_collection = yamlCollection;
  const normalized = new Map();
  for (const source of input.documents) {
    const normalizedPath = store.handelize(source.path);
    if (normalized.has(normalizedPath)) result.errors.push(
      `QMD path collision: ${source.path} and ${normalized.get(normalizedPath)}`);
    normalized.set(normalizedPath, source.path);
  }
  const docQuery = db.prepare(`SELECT d.*, c.doc AS body FROM documents d
    LEFT JOIN content c ON c.hash=d.hash WHERE d.collection=? AND d.path=?`);
  const ftsQuery = db.prepare('SELECT filepath,title,body FROM documents_fts WHERE rowid=?');
  const metadataQuery = db.prepare('SELECT * FROM content_vectors WHERE hash=? ORDER BY seq');
  const vectorQuery = db.prepare('SELECT embedding FROM vectors_vec WHERE hash_seq=?');
  const embeddingCache = new Map();
  function checkEmbeddings(hash, body) {
    if (embeddingCache.has(hash)) return embeddingCache.get(hash);
    const metadata = metadataQuery.all(hash);
    const current = metadata.filter(v => v.model === model && v.embed_fingerprint === fingerprint);
    const expected = [...new Set(current.map(v => v.total_chunks))];
    const issues = [];
    if (!current.length) issues.push('no_current_embeddings');
    if (expected.length !== 1 || !Number.isInteger(expected[0]) || expected[0] < 1)
      issues.push('inconsistent_or_missing_total_chunks');
    const n = expected.length === 1 ? expected[0] : null;
    if (n !== null && (current.length !== n || current.some((v, i) => v.seq !== i)))
      issues.push('incomplete_chunk_sequence');
    if (metadata.length !== current.length) issues.push('obsolete_model_or_fingerprint_chunks');
    const proofs = [];
    let priorPosition = -1;
    for (const v of current) {
      const row = vectorQuery.get(`${hash}_${v.seq}`);
      const vector = row?.embedding;
      let finite = false, nonzero = false;
      if (vector && vector.length === dimensions * 4) {
        finite = true;
        for (let offset = 0; offset < vector.length; offset += 4) {
          const value = vector.readFloatLE(offset);
          if (!Number.isFinite(value)) finite = false;
          if (value !== 0) nonzero = true;
        }
      }
      const validPosition = Number.isInteger(v.pos) && v.pos >= 0 && v.pos < body.length &&
        (v.seq === 0 ? v.pos === 0 : v.pos > priorPosition);
      priorPosition = v.pos;
      if (!vector) issues.push(`missing_vector:${v.seq}`);
      else if (!finite || !nonzero) issues.push(`invalid_vector:${v.seq}`);
      if (!validPosition) issues.push(`invalid_chunk_position:${v.seq}`);
      proofs.push({ seq: v.seq, pos: v.pos, embedded_at: v.embedded_at,
        vector_present: !!vector, vector_bytes: vector?.length || 0,
        finite, nonzero, vector_sha256: vector ? sha(vector) : null });
    }
    const checked = { passed: issues.length === 0, errors: issues,
      content_hash: hash, model, fingerprint, expected_chunks: n,
      current_metadata_chunks: current.length, all_metadata_chunks: metadata.length,
      actual_vector_chunks: proofs.filter(v => v.vector_present).length,
      obsolete_metadata: metadata.filter(v => v.model !== model || v.embed_fingerprint !== fingerprint),
      chunks: proofs };
    embeddingCache.set(hash, checked);
    return checked;
  }
  for (const source of input.documents) {
    const item = { ...source, normalized_path: store.handelize(source.path), errors: [] };
    const sourcePath = path.join(input.root, source.path);
    if (!fs.existsSync(sourcePath)) {
      item.errors.push('missing_source_file');
      item.passed = false;
      result.documents.push(item);
      continue;
    }
    const real = fs.realpathSync(sourcePath);
    if (!real.startsWith(input.root + path.sep)) item.errors.push('source_resolves_outside_repository');
    const raw = fs.readFileSync(sourcePath);
    const body = raw.toString('utf8');
    item.disk_sha256 = sha(raw);
    item.qmd_expected_hash = await store.hashContent(body);
    item.disk_bytes = raw.length;
    if (!raw.equals(Buffer.from(body, 'utf8'))) item.errors.push('invalid_utf8');
    if (!body.trim()) item.errors.push('empty_source_file');
    if (!picomatch(collection.pattern)(source.path) ||
        [...ignores, ...yamlIgnores].some(glob => picomatch(glob)(source.path)))
      item.errors.push('excluded_by_collection_configuration');
    const doc = docQuery.get('context', item.normalized_path);
    item.document_id = doc?.id ?? null;
    item.indexed_hash = doc?.hash ?? null;
    item.active = doc?.active === 1;
    item.hash_matches = doc?.hash === item.qmd_expected_hash;
    item.body_matches = doc?.body === body;
    item.title_matches = doc?.title === store.extractTitle(body, source.path);
    if (!doc) item.errors.push('missing_index_document');
    else {
      if (!item.active) item.errors.push('inactive_index_document');
      if (!item.hash_matches || !item.body_matches) item.errors.push('stale_index_text');
      if (!item.title_matches) item.errors.push('stale_index_title');
      const fts = ftsQuery.get(doc.id);
      item.fts_body_matches = fts?.body === store.normalizeCjkForFTS(body);
      item.fts_title_matches = fts?.title === store.normalizeCjkForFTS(store.extractTitle(body, source.path));
      item.fts_path_matches = fts?.filepath === store.normalizeCjkForFTS(`context/${item.normalized_path}`);
      if (!item.fts_body_matches || !item.fts_title_matches || !item.fts_path_matches)
        item.errors.push('missing_or_stale_fts_row');
    }
    // Check the CURRENT FILE hash even if documents still points at an older hash.
    // A stale document with complete old vectors must never pass this audit.
    item.embeddings = checkEmbeddings(item.qmd_expected_hash, body);
    if (!item.embeddings.passed) item.errors.push('missing_or_incomplete_current_embeddings');
    item.passed = item.errors.length === 0;
    result.documents.push(item);
  }
  result.runtime.config_unchanged_during_audit = configHash ===
    (fs.existsSync(configPath) ? sha(fs.readFileSync(configPath)) : null);
  if (!result.runtime.config_unchanged_during_audit) result.errors.push('QMD config changed during audit');
  // This is the installed QMD pending predicate, strengthened above with actual
  // vectors, contiguous sequences, coherent totals, and current disk text.
  result.index_pending = db.prepare(`SELECT d.path,d.hash FROM documents d LEFT JOIN
    (SELECT hash,COUNT(*) chunk_count,MAX(total_chunks) expected_chunks FROM content_vectors
     WHERE model=? AND embed_fingerprint=? GROUP BY hash) v ON d.hash=v.hash
    WHERE d.collection='context' AND d.active=1
    AND (v.hash IS NULL OR v.chunk_count<v.expected_chunks) ORDER BY d.path`).all(model,fingerprint);
  result.required_index_pending = result.index_pending.filter(r => normalized.has(r.path));
  result.index_totals = {
    active_documents: db.prepare('SELECT COUNT(*) n FROM documents WHERE active=1').get().n,
    required_unique_current_hashes: embeddingCache.size,
    vector_metadata: db.prepare('SELECT COUNT(*) n FROM content_vectors').get().n,
    actual_vectors: db.prepare('SELECT COUNT(*) n FROM vectors_vec').get().n
  };
} finally {
  db.exec('ROLLBACK');
  db.close();
}
process.stdout.write(JSON.stringify(result));
'''


def run(args, **kwargs):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True, **kwargs).stdout.strip()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def discover_scope():
    documents = {}
    manifests = {}
    for relative, category, count in [(LI_MANIFEST, 'linkedin_post', 914),
                                       (YT_MANIFEST, 'youtube_transcript', 100)]:
        file = ROOT / relative
        rows = json.loads(file.read_text())
        if len(rows) != count or len({r['id'] for r in rows}) != count:
            raise ValueError(f'{relative}: expected exactly {count} unique selected sources')
        manifests[relative] = digest(file)
        for row in rows:
            source = row['markdown_path']
            if source in documents:
                raise ValueError(f'Duplicate selected source path: {source}')
            if Path(source).is_absolute() or '..' in Path(source).parts or not source.endswith('.md'):
                raise ValueError(f'Invalid source path: {source}')
            documents[source] = {'path': source, 'category': category, 'source_id': row['id']}
    for relative in ('index.md', 'log.md'):
        documents[relative] = {'path': relative, 'category': 'root_context'}
    discovered = []
    for folder in (*WIKI_ROOTS, 'raw'):
        for directory, dirs, files in os.walk(ROOT / folder, followlinks=False):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in EXCLUDED_PARTS
                       and not (Path(directory) / d).is_symlink()]
            for name in files:
                if name.endswith('.md') and not name.startswith('.'):
                    discovered.append((Path(directory) / name).relative_to(ROOT).as_posix())
    # Match the repository's ignored-output policy, including future additions.
    ignored_result = subprocess.run(['git', 'check-ignore', '--stdin', '-z'], cwd=ROOT,
                                    input='\0'.join(discovered + list(documents)) + '\0',
                                    text=True, capture_output=True)
    if ignored_result.returncode not in (0, 1):
        raise RuntimeError(f'git check-ignore failed: {ignored_result.stderr}')
    ignored = set(filter(None, ignored_result.stdout.split('\0')))
    if ignored & documents.keys():
        raise ValueError(f'Required selected/root files are ignored: {sorted(ignored & documents.keys())}')
    for relative in discovered:
        if relative not in ignored and relative not in documents:
            documents[relative] = {'path': relative, 'category':
                                  'raw_supplement' if relative.startswith('raw/') else 'wiki_context'}
    return sorted(documents.values(), key=lambda d: d['path']), manifests, sorted(ignored)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'research/qmd-coverage-audit.json')
    args = parser.parse_args()
    report = {'audit_version': 1, 'started_at': dt.datetime.now(dt.timezone.utc).isoformat(),
              'repository': str(ROOT), 'status': 'error', 'read_only_index_access': True,
              'discovery_exclusions': sorted(EXCLUDED_PARTS) + ['hidden paths', 'git-ignored files'],
              'proof_boundary': 'Checks exact current UTF-8 content, FTS rows and every stored vector '
                                'chunk under the installed runtime fingerprint. Chunk completeness '
                                'uses coherent total_chunks and contiguous sequence metadata, with '
                                'actual finite nonzero vector rows. Does not regenerate embeddings '
                                'or certify their semantic quality.'}
    exit_code = 2
    try:
        wrapper = ROOT / 'scripts/qmd.sh'
        index = run([str(wrapper), '--print-index'])
        expected = 'content-engine-' + hashlib.sha256(str(ROOT).encode()).hexdigest()[:16]
        if index != expected:
            raise ValueError(f'Wrapper index {index!r} does not match checkout identity {expected!r}')
        version = run([str(wrapper), '--version'])
        help_output = run([str(wrapper), '--help'])
        matches = re.findall(r'^Index:\s*(.+)$', re.sub(r'\x1b\[[0-9;]*m', '', help_output), re.M)
        if len(matches) != 1:
            raise ValueError('Cannot derive unique database path from installed QMD help')
        database = Path(matches[0]).expanduser().resolve(strict=True)
        if database.name != index + '.sqlite':
            raise ValueError(f'Unexpected index database name: {database}')
        executable = shutil.which('qmd')
        if not executable:
            raise ValueError('qmd is not installed')
        entry = Path(executable).resolve()
        package = next((p for p in entry.parents if (p / 'package.json').exists()
                        and json.loads((p / 'package.json').read_text()).get('name') == '@tobilu/qmd'), None)
        if package is None:
            raise ValueError('Cannot locate the installed @tobilu/qmd package')
        # Mirror the wrapper's matching Node selection, without shell evaluation.
        prefix = str(entry).split('/lib/node_modules/', 1)[0]
        node = Path(prefix) / 'bin/node'
        if not node.is_file():
            node = Path(shutil.which('node') or '')
        if not node.is_file():
            raise ValueError('Cannot locate the Node runtime used by scripts/qmd.sh')
        documents, manifests, ignored = discover_scope()
        report.update({'index_name': index, 'database_path': str(database), 'qmd_version': version,
                       'qmd_package_root': str(package), 'node_runtime': str(node),
                       'wrapper_sha256': digest(wrapper), 'selection_manifest_sha256': manifests,
                       'excluded_ignored_markdown': ignored,
                       'scope_policy': 'combined 914 LinkedIn records (including 3 empty-body records) + selected 100 transcripts + all six wiki roots + index/log + supplementary raw Markdown'})
        payload = {'root': str(ROOT), 'package_root': str(package), 'index_name': index,
                   'database_path': str(database), 'documents': documents}
        result = subprocess.run([str(node), '--input-type=module', '-e', NODE_AUDIT], cwd=ROOT,
                                input=json.dumps(payload), text=True, capture_output=True, timeout=120)
        if result.returncode:
            raise RuntimeError(f'Installed-runtime read-only audit failed: {result.stderr.strip()}')
        report.update(json.loads(result.stdout))
        # Catch source edits or new required pages while the read snapshot ran.
        after_documents, after_manifests, _ = discover_scope()
        if documents != after_documents or manifests != after_manifests:
            report['errors'].append('Required scope or selection manifests changed during audit; rerun')
        for item in report['documents']:
            source = ROOT / item['path']
            if item.get('disk_sha256') and (not source.exists() or digest(source) != item['disk_sha256']):
                item['errors'].append('source_changed_during_audit')
                item['passed'] = False
        by_category = {}
        for category in sorted({d['category'] for d in documents}):
            members = [d for d in report['documents'] if d['category'] == category]
            by_category[category] = {'required': len(members),
                                     'passed': sum(bool(d['passed']) for d in members),
                                     'failed': sum(not d['passed'] for d in members)}
        failures = [d for d in report['documents'] if not d['passed']]
        report['summary'] = {'required_documents': len(documents),
                             'passed_documents': len(documents) - len(failures),
                             'failed_documents': len(failures), 'by_category': by_category,
                             'required_index_pending': len(report['required_index_pending']),
                             'required_missing_or_stale_embeddings': sum(
                                 not d.get('embeddings', {}).get('passed', False) for d in report['documents']),
                             'failure_reasons': dict(collections.Counter(
                                 error for item in failures for error in item['errors']))}
        passed = not failures and not report['errors'] and not report['required_index_pending']
        report['status'] = 'passed' if passed else 'failed'
        exit_code = 0 if passed else 1
    except Exception as exc:
        report['fatal_error'] = str(exc)
    report['finished_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=output.parent, delete=False) as temporary:
        json.dump(report, temporary, indent=2, ensure_ascii=False)
        temporary.write('\n')
        temporary_path = Path(temporary.name)
    temporary_path.replace(output)
    print(json.dumps({'status': report['status'], 'audit': str(output),
                      'summary': report.get('summary'), 'errors': report.get('errors', []),
                      'fatal_error': report.get('fatal_error')}, indent=2))
    return exit_code


if __name__ == '__main__':
    sys.exit(main())
