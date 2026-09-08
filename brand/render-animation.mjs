// Render a local GraphicMotion scene to GIF, MP4, PNG and a pinned editable bundle.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import {chromium} from 'playwright';
import ffmpeg from 'ffmpeg-static';
import {glyphFonts, textBounds} from './browser.mjs';

const brand = path.dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
if (args.length < 2) throw Error('Usage: node brand/render-animation.mjs <animation.json> <output-directory> [--keep-frames]');
const configFile = await fs.realpath(path.resolve(args[0]));
const config = JSON.parse(await fs.readFile(configFile, 'utf8'));
const entry = await fs.realpath(path.resolve(path.dirname(configFile), config.entry));
const inside = (root, file) => file.startsWith(root + path.sep);
if (!inside(brand, entry) || !inside(brand, configFile)) throw Error('Scene and config must be inside brand/.');
for (const field of ['width', 'height', 'duration', 'fps', 'gifWidth', 'gifFps', 'posterMs']) {
  if (!Number.isFinite(config[field]) || config[field] <= 0) throw Error(`Invalid ${field}`);
}
if (![config.width, config.height, config.gifWidth].every(Number.isInteger) || config.width % 2 || config.height % 2) throw Error('Native dimensions must be even integers.');
if (![10,20,25].includes(config.gifFps)) throw Error('GIF fps must be 10, 20 or 25 for exact centisecond timing.');
if (config.posterMs > config.duration || config.gifWidth > config.width) throw Error('Poster time or GIF size outside scene.');
const count = config.duration * config.fps / 1000;
if (!Number.isInteger(count) || !Number.isInteger(config.duration * config.gifFps / 1000)) throw Error('Duration must contain whole frames at both frame rates.');
if (!Array.isArray(config.fontFamilies) || !config.fontFamilies.length) throw Error('Specify expected custom fontFamilies.');
if (!Array.isArray(config.sourceFiles)) throw Error('Specify the sourceFiles dependency allowlist.');
const sourceFiles = [...new Set([path.relative(brand, configFile), ...config.sourceFiles])];
const sources = [];
for (const name of sourceFiles) {
  const file = await fs.realpath(path.resolve(brand, name));
  if (!inside(brand, file) || file !== path.resolve(brand, name)) throw Error(`Source escapes brand or is a symlink: ${name}`);
  sources.push({file, name: path.relative(brand, file), sha256: digest(await fs.readFile(file))});
}
const requestedOutput = path.resolve(args[1]);
// Resolve the existing ancestor before mkdir, including symlinked destinations.
let ancestor = requestedOutput;
while (!(await fs.stat(ancestor).catch(() => null))) ancestor = path.dirname(ancestor);
const projected = path.resolve(await fs.realpath(ancestor), path.relative(ancestor, requestedOutput));
if (projected === brand || inside(brand, projected) || inside(projected, brand)) throw Error('Output must be separate from the brand source tree.');
await fs.mkdir(projected, {recursive:true});
const out = await fs.realpath(projected);
const temp = await fs.mkdtemp(path.join(out, '.capture-'));
const errors = [], requested = new Set();
const browser = await chromium.launch({headless:true});
let success = false;
function digest(bytes) { return crypto.createHash('sha256').update(bytes).digest('hex'); }
function escapeHTML(value) { return String(value).replace(/[&<>"']/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[character])); }
const reviewTitle = escapeHTML(config.title || 'Graphic review');
const reviewDescription = escapeHTML(config.description || 'Local graphic export.');
async function encode(args) {
  return new Promise((resolve,reject) => {
    const child = spawn(ffmpeg, ['-hide_banner','-loglevel','error', ...args], {stdio:['ignore','pipe','pipe']});
    let stdout = '', stderr = '';
    child.stdout.on('data', chunk => { stdout += chunk; });
    child.stderr.on('data', chunk => { stderr += chunk; });
    child.on('error', reject);
    child.on('close', code => code === 0 ? resolve(stdout) : reject(Error(stderr || `FFmpeg exited ${code}`)));
  });
}
async function decoded(file) {
  const result = await encode(['-i',file,'-map','0:v:0','-fps_mode','passthrough','-f','framemd5','-']);
  const timebase = result.match(/#tb 0:\s*(\d+)\/(\d+)/);
  const dimensions = result.match(/#dimensions 0:\s*(\d+)x(\d+)/);
  const rows = result.split('\n').filter(line => /^0,/.test(line)).map(line => line.split(',').map(part => part.trim()));
  if (!timebase || !dimensions || !rows.length) throw Error(`Cannot inspect decoded frames: ${file}`);
  const last = rows.at(-1), duration = (Number(last[2]) + Number(last[3]) - Number(rows[0][2])) * Number(timebase[1]) / Number(timebase[2]);
  return {dimensions:dimensions.slice(1).map(Number), frames:rows.length, durationSeconds:duration};
}
try {
  const page = await browser.newPage({viewport:{width:config.width,height:config.height},deviceScaleFactor:1});
  await page.context().setOffline(true);
  page.on('pageerror', error => errors.push(error.message));
  page.on('request', request => {
    const url = new URL(request.url());
    if (url.protocol === 'file:') requested.add(fileURLToPath(url));
    else if (!['data:','blob:'].includes(url.protocol)) errors.push(`Non-local resource: ${url.href}`);
  });
  page.on('requestfailed', request => errors.push(`Missing asset: ${request.url()}`));
  await page.goto(pathToFileURL(entry).href);
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all([...document.images].map(image => image.decode()));
    if (!window.GraphicMotion) throw Error('Missing GraphicMotion API');
    await GraphicMotion.ready;
    GraphicMotion.pause();
  });
  const selector = config.selector || '.ms-art';
  const art = page.locator(selector);
  const api = await page.evaluate(() => ({duration:GraphicMotion.duration,posterMs:GraphicMotion.posterMs}));
  if (api.duration !== config.duration || api.posterMs !== config.posterMs) throw Error('Config and timeline disagree.');
  const bounds = await art.boundingBox();
  if (bounds.width !== config.width || bounds.height !== config.height) throw Error('Canvas dimensions disagree with config.');
  const seek = async (ms, reduced = false) => page.evaluate(({ms,reduced}) => GraphicMotion.seek(ms,{respectReducedMotion:reduced}), {ms,reduced});
  await seek(config.posterMs);
  const fonts = await glyphFonts(page, selector);
  if (!fonts.length || fonts.some(font => !font.isCustomFont || !config.fontFamilies.includes(font.familyName))) throw Error(`Unexpected rendered font: ${JSON.stringify(fonts)}`);
  const poster = await art.screenshot({path:path.join(out,'poster.png')});
  const probe = Math.round(config.duration * 0.41);
  await seek(probe); const first = await art.screenshot();
  await seek(config.duration * 0.8); await seek(0); await seek(probe);
  if (digest(first) !== digest(await art.screenshot())) throw Error('Backward/repeated seek changes pixels.');
  await page.emulateMedia({reducedMotion:'reduce'});
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  await seek(0,true);
  const reducedPoster = await art.screenshot();
  if (digest(poster) !== digest(reducedPoster)) {
    await fs.writeFile(path.join(temp,'reduced-motion.png'),reducedPoster);
    throw Error('Reduced motion must show the complete poster state.');
  }
  await page.emulateMedia({reducedMotion:'no-preference'});
  await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
  await seek(0); const opening = digest(await art.screenshot());
  await seek(config.duration); const ending = digest(await art.screenshot());
  if (config.seamless && opening !== ending) throw Error('Claimed seamless loop has unequal endpoint pixels.');
  const layout = [], intentionalClips = [];
  const reviewTimes = [...new Set([0,...(config.reviewTimes || []),config.posterMs,config.duration])].sort((a,b) => a-b);
  await fs.mkdir(path.join(out,'review'), {recursive:true});
  for (let i = 0; i < reviewTimes.length; i++) {
    const ms = reviewTimes[i];
    if (ms < 0 || ms > config.duration) throw Error('Review timestamp outside duration.');
    await seek(ms);
    const problems = (await textBounds(page,selector)).filter(problem => {
      const declared = ms !== config.posterMs && (config.motionClipClasses || []).some(name => problem.reason === `clipped by ${name}`);
      if (declared) intentionalClips.push({ms,...problem});
      return !declared;
    });
    if (problems.length) layout.push({ms,problems});
    await art.screenshot({path:path.join(out,'review',`${String(i).padStart(2,'0')}.png`)});
  }
  if (layout.length) throw Error(`Text bounds: ${JSON.stringify(layout)}`);
  for (let i = 0; i < count; i++) {
    await seek(i * 1000 / config.fps);
    await art.screenshot({path:path.join(temp,`${String(i).padStart(5,'0')}.png`)});
    if (i % config.fps === 0) console.log(`Capture ${i / config.fps}s / ${config.duration / 1000}s`);
  }
  const allowed = new Set(sources.map(source => source.file));
  for (const file of requested) if (!allowed.has(await fs.realpath(file))) errors.push(`Missing from editable bundle: ${path.relative(brand,file)}`);
  if (errors.length) throw Error(errors.join('\n'));
  const input = ['-y','-framerate',String(config.fps),'-i',path.join(temp,'%05d.png')];
  await encode([...input,'-frames:v',String(count),'-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',path.join(out,'graphic.mp4')]);
  const gifHeight = Math.round(config.height * config.gifWidth / config.width);
  const gifFilter = `fps=${config.gifFps},scale=${config.gifWidth}:${gifHeight}:flags=lanczos,split[a][b];[a]palettegen=max_colors=256:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle`;
  await encode([...input,'-filter_complex',gifFilter,'-loop','0',path.join(out,'graphic.gif')]);
  await encode(['-y','-i',path.join(out,'poster.png'),'-vf','scale=360:-1:flags=lanczos','-frames:v','1',path.join(out,'poster-phone.png')]);
  const columns = 4, rows = Math.ceil(reviewTimes.length / columns);
  await encode(['-y','-framerate','1','-i',path.join(out,'review','%02d.png'),'-vf',`scale=270:-1,tile=${columns}x${rows}:padding=8:color=0x1e1e1e`,'-frames:v','1',path.join(out,'contact-sheet.png')]);
  const mp4 = await decoded(path.join(out,'graphic.mp4'));
  const gif = await decoded(path.join(out,'graphic.gif'));
  for (const [format,meta,dims,expected] of [['mp4',mp4,[config.width,config.height],count],['gif',gif,[config.gifWidth,gifHeight],config.duration*config.gifFps/1000]]) {
    if (String(meta.dimensions) !== String(dims) || meta.frames !== expected || Math.abs(meta.durationSeconds - config.duration/1000) > 0.025) throw Error(`Encoded ${format} mismatch: ${JSON.stringify(meta)}`);
  }
  const bundle = await fs.mkdtemp(path.join(out,'editable-'));
  for (const source of sources) {
    const dest = path.join(bundle,'brand',source.name);
    await fs.mkdir(path.dirname(dest), {recursive:true});
    await fs.copyFile(source.file,dest);
  }
  const bundledEntry = path.join(bundle,'brand',path.relative(brand,entry));
  await page.goto(pathToFileURL(bundledEntry).href);
  await page.evaluate(async () => { await document.fonts.ready; await GraphicMotion.ready; GraphicMotion.pause(); GraphicMotion.seek(GraphicMotion.posterMs,{respectReducedMotion:false}); });
  if (digest(poster) !== digest(await page.locator(selector).screenshot())) throw Error('Editable bundle does not reproduce the poster.');
  if (errors.length) throw Error(errors.join('\n'));
  const exports = {};
  for (const name of ['graphic.gif','graphic.mp4','poster.png','poster-phone.png','contact-sheet.png']) {
    const bytes = await fs.readFile(path.join(out,name)); exports[name] = {bytes:bytes.length,sha256:digest(bytes)};
  }
  const report = {config,mp4,gif,fonts,reviewTimes,errors,layout,intentionalClips,deterministicSeek:true,reducedMotion:true,endpointPixelsMatch:opening===ending,bundlePosterMatches:true,editableEntry:path.relative(out,bundledEntry),sources:sources.map(({name,sha256})=>({name,sha256})),exports};
  await fs.writeFile(path.join(out,'export-report.json'),JSON.stringify(report,null,2)+'\n');
  await fs.writeFile(path.join(out,'review.html'),`<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Graphic review</title><style>body{margin:32px;background:#0a0b0e;color:#f1f5f9;font:16px system-ui}a{color:#f4805d}section{display:flex;flex-wrap:wrap;gap:24px}figure{margin:0}video,img{display:block;width:min(360px,85vw);height:auto}figcaption{margin:12px 0}button{font:inherit;margin:12px 0}</style><h1>${reviewTitle}</h1><p>${reviewDescription}</p><p><a href="${path.relative(out,bundledEntry).split(path.sep).join('/')}">Editable HTML / play, pause and scrub</a> · <a href="export-report.json">Export details</a></p><section><figure><video controls loop playsinline preload="metadata" poster="poster.png" src="graphic.mp4"></video><figcaption>MP4 · ${config.width} × ${config.height}</figcaption></figure><figure><img id="gif" src="poster-phone.png" alt="Workflow illustration poster"><button id="toggle" type="button">Play GIF</button><figcaption>GIF · ${config.gifWidth} × ${gifHeight}</figcaption></figure><figure><img src="poster.png" alt="Complete workflow illustration"><figcaption>Static PNG</figcaption></figure></section><script>let playing=false;document.querySelector('#toggle').onclick=()=>{playing=!playing;document.querySelector('#gif').src=playing?'graphic.gif':'poster-phone.png';document.querySelector('#toggle').textContent=playing?'Stop GIF':'Play GIF';};</script></html>`);
  console.log(JSON.stringify({output:out,mp4,gif,gifBytes:exports['graphic.gif'].bytes,editableEntry:report.editableEntry},null,2));
  success = true;
} finally {
  await browser.close();
  if (success && !args.includes('--keep-frames')) await fs.rm(temp,{recursive:true});
  else console.log(`Capture frames retained: ${temp}`);
}
