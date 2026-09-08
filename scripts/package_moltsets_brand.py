#!/usr/bin/env python3
"""Package the self-contained production kit, excluding source fonts and dependencies."""
from pathlib import Path
import hashlib,json,zipfile,tempfile

ROOT=Path(__file__).resolve().parents[1]
BRAND=ROOT/'brand'
OUT=ROOT/'output/moltsets-brand'
OUT.mkdir(parents=True,exist_ok=True)
allowed_dirs={'assets','evidence','kit','motion','templates'}
allowed_root={'BRAND.md','architecture.md','patterns.md','package.json','package-lock.json','tokens.json','tokens.css','tokens.js','base.css','components.css','components.mjs','components-manifest.json','build.mjs','browser.mjs','render.mjs','check.mjs'}
files=[]
for p in sorted(BRAND.rglob('*')):
    rel=p.relative_to(BRAND)
    if not p.is_file() or 'node_modules' in rel.parts or p.name.startswith('.'):continue
    if rel.parts[0] in allowed_dirs or rel.as_posix() in allowed_root:files.append(p)
assert files and all('SF-Mono' not in p.name for p in files)
manifest={'version':json.loads((BRAND/'tokens.json').read_text())['version'],'scope':'Production kit; reference-only SF Mono archive excluded. Company asset rights retained.','files':[{'path':'brand/'+p.relative_to(BRAND).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
target=OUT/'moltsets-graphics-kit.zip'
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
    for p in files:z.write(p,'brand/'+p.relative_to(BRAND).as_posix())
    z.writestr('manifest.json',json.dumps(manifest,indent=2)+'\n')
    z.writestr('START-HERE.txt','Open brand/kit/index.html in a browser. Everything for the visual kit works offline.\nFor editing and rendering, read brand/architecture.md. Install dependencies using the included package lock.\nCompany source evidence under raw/ remains in the original repository. Production asset URLs and hashes are in brand/assets/manifest.json; palette evidence is in brand/evidence/source-tokens.json.\nThis is a company graphics kit, not a stock asset licence or approved campaign.\n')
with tempfile.TemporaryDirectory(prefix='moltsets-kit-') as temp:
    with zipfile.ZipFile(target) as z:z.extractall(temp)
    for record in manifest['files']:
        assert hashlib.sha256((Path(temp)/record['path']).read_bytes()).hexdigest()==record['sha256']
(OUT/'package-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Packaged and hash-verified {len(files)} files: {target}')
