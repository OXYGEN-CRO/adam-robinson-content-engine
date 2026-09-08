import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {execFile} from 'node:child_process';
import {promisify} from 'node:util';
import crypto from 'node:crypto';
import ffmpeg from 'ffmpeg-static';
import {environment,root,output,settle,glyphFonts,textBounds,sourceDigest} from './browser.mjs';
const run=promisify(execFile);
const read=p=>fs.readFile(path.join(root,p),'utf8');
const tokens=JSON.parse(await read('tokens.json'));
const templates=JSON.parse(await read('templates/manifest.json'));
const components=JSON.parse(await read('components-manifest.json'));
const source=JSON.parse(await read('evidence/source-tokens.json'));
const css=await read('tokens.css');
const checks=[];
const currentSource=await sourceDigest();
function pass(name){checks.push(name);console.log('PASS '+name);}
for(const [key,value] of Object.entries(tokens.colors)){
 assert(css.includes(`--ms-${key}: ${value};`),`Generated token drift: ${key}`);
 const original=source[key];const normalized=original.startsWith('rgb(')?'#'+original.match(/\d+/g).map(v=>Number(v).toString(16).padStart(2,'0')).join('').toUpperCase():original;
 assert.equal(value,normalized,`Source colour changed: ${key}`);
}
assert.equal(JSON.parse((await read('tokens.js')).split('window.MoltsetsTokens = ')[1].replace(/;\s*$/,'' )).version,tokens.version);
assert.deepEqual(JSON.parse((await read('tokens.js')).split('window.MoltsetsTokens = ')[1].replace(/;\s*$/,'' )),tokens);
for(const [role,spec] of Object.entries(tokens.type))for(const [key,value] of Object.entries(spec))assert(css.includes(`--ms-${role}-${key}: ${value}${key==='size'?'px':key==='tracking'?'em':''};`));
pass(`${Object.keys(tokens.colors).length} exact source colours and generated token adapters`);
assert((await read('assets/fonts/RobotoMono-OFL.txt')).includes('SIL OPEN FONT LICENSE Version 1.1'));
assert(!/SF-Mono.*\.(woff|ttf|otf)/i.test(css));
for(const asset of JSON.parse(await read('assets/manifest.json'))){const bytes=await fs.readFile(path.resolve(root,asset.file));assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),asset.sha256,asset.file);}
pass('Source assets unchanged; licensed production font bundled separately');
function dimensions(bytes){assert.equal(bytes.toString('hex',0,8),'89504e470d0a1a0a');return [bytes.readUInt32BE(16),bytes.readUInt32BE(20)];}
for(const t of templates)assert.deepEqual(dimensions(await fs.readFile(path.join(output,t.id+'.png'))),[t.width,t.height]);
for(const c of components)assert.deepEqual(dimensions(await fs.readFile(path.join(output,'components',c.id+'.png'))),[c.width,c.height]);
pass(`${templates.length} exported templates and ${components.length} component PNG dimensions`);
const luminance=hex=>{const c=hex.slice(1).match(/../g).map(v=>parseInt(v,16)/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4);return c[0]*.2126+c[1]*.7152+c[2]*.0722;};
const pairs=[];
for(const bg of ['bg-base','bg-elevated','brand-bg'])for(const fg of ['fg-primary','fg-secondary','fg-muted','brand','success','hint','danger']){const a=luminance(tokens.colors[fg]),b=luminance(tokens.colors[bg]);const ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);assert(ratio>=4.5,`${fg}/${bg}: ${ratio}`);pairs.push({fg,bg,ratio:Number(ratio.toFixed(2))});}
assert((luminance(tokens.colors.brand)+.05)/(luminance(tokens.colors['bg-base'])+.05)>=4.5);
pass('21 designated reading pairs and dark-on-coral CTA contrast');
const env=await environment();
try{
 for(const t of templates){
  const page=await env.browser.newPage({viewport:{width:t.width,height:t.height}});const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)errors.push(r.url());});
  await page.goto(`${env.base}/${t.file}`);await settle(page);assert.deepEqual(await textBounds(page),[],t.id);
  const safe=await page.evaluate(()=>{const art=document.querySelector('.ms-art'),r=art.getBoundingClientRect(),c=getComputedStyle(art);return [...art.children].filter(el=>getComputedStyle(el).position!=='absolute').flatMap(el=>{const a=el.getBoundingClientRect();return a.left<r.left+parseFloat(c.paddingLeft)-2||a.right>r.right-parseFloat(c.paddingRight)+2||a.top<r.top+parseFloat(c.paddingTop)-2||a.bottom>r.bottom-parseFloat(c.paddingBottom)+2?[{element:el.tagName,class:el.className,bottom:a.bottom,limit:r.bottom-parseFloat(c.paddingBottom)}]:[];});});
  assert.deepEqual(safe,[],`${t.id} safe area`);
  const fonts=await glyphFonts(page,'.ms-art');assert(fonts.length>0,t.id+' has no rendered glyphs');assert(fonts.every(f=>f.familyName==='Roboto Mono'&&f.isCustomFont),t.id+': '+JSON.stringify(fonts));
  const alpha=await page.evaluate(async src=>{const im=new Image();im.src=src;await im.decode();const c=document.createElement('canvas');c.width=im.naturalWidth;c.height=im.naturalHeight;const x=c.getContext('2d');x.drawImage(im,0,0);return x.getImageData(0,0,1,1).data[3];},`${env.base}/assets/logos/moltsets-lockup-source.png`);assert.equal(alpha,0,'Logo background');
  assert.deepEqual(errors,[],t.id+' requests');await page.close();
 }
 pass('All scenes: real font glyphs, decoded assets, text bounds, safe margins, no load errors');
 const motion=await env.browser.newPage({viewport:{width:1920,height:1080}});await motion.goto(`${env.base}/templates/workflow.html`);await settle(motion);
 const snapshots=[];
 for(const time of [0,600,1400,2800,4000]){await motion.evaluate(ms=>MoltsetsMotion.seek(ms),time);snapshots.push({time,state:await motion.evaluate(()=>[...document.querySelectorAll('[data-enter]')].map(e=>e.style.opacity)),hash:crypto.createHash('sha256').update(await motion.screenshot()).digest('hex')});}
 assert(new Set(snapshots.map(s=>s.hash)).size>=4,'Motion frames must differ');
 await motion.evaluate(()=>MoltsetsMotion.seek(1400));assert.equal(crypto.createHash('sha256').update(await motion.screenshot()).digest('hex'),snapshots.find(s=>s.time===1400).hash,'Backward seek must match');
 await motion.emulateMedia({reducedMotion:'reduce'});await motion.evaluate(()=>MoltsetsMotion.seek(0));assert((await motion.evaluate(()=>[...document.querySelectorAll('[data-enter]')].map(e=>e.style.opacity))).every(v=>v==='1'));
 pass('Motion forward/backward seek, visibly changing frames, reduced-motion final state');
 const sprites=await env.browser.newPage();await sprites.goto(`${env.base}/templates/cover.html`);await settle(sprites);await sprites.evaluate(()=>MoltsetsMotion.seek(150));assert((await sprites.locator('[data-mascot]').getAttribute('src')).endsWith('step-2.svg'));await sprites.evaluate(()=>MoltsetsMotion.seek(550));assert((await sprites.locator('[data-mascot]').getAttribute('src')).endsWith('step-final.svg'));
 await sprites.evaluate(()=>{const im=document.createElement('img');im.dataset.thinking='';document.body.append(im);MoltsetsMotion.seek(95);});assert((await sprites.locator('[data-thinking]').getAttribute('src')).endsWith('frame-2.svg'));await sprites.evaluate(()=>MoltsetsMotion.seek(0));assert((await sprites.locator('[data-thinking]').getAttribute('src')).endsWith('frame-1.svg'));pass('Original mascot and deterministic thinking frame timing');
 const kit=await env.browser.newPage({viewport:{width:1440,height:1000}});await kit.goto(`${env.base}/kit/index.html`);await settle(kit);
 for(const width of [1440,768,390]){await kit.setViewportSize({width,height:900});assert(await kit.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Kit horizontal overflow at '+width);}
 await kit.locator('details').first().locator('summary').click();assert(await kit.locator('details').first().evaluate(e=>e.open));
 await kit.goto(`${env.base}/kit/motion.html`);await kit.locator('iframe').waitFor();const preview=kit.frames().find(f=>f.url().includes('/templates/workflow.html'));await preview.waitForFunction(()=>window.MoltsetsMotion);
 await kit.locator('#time').fill('1400');await preview.waitForFunction(()=>MoltsetsMotion.current===1400);
 await kit.locator('#play').click();await preview.waitForFunction(()=>MoltsetsMotion.current<1400);await kit.locator('#pause').click();
 pass('Responsive catalogue, markup disclosure, motion scrubbing and playback controls');
 await kit.goto(pathToFileURL(path.join(root,'kit/motion.html')).href);await kit.locator('iframe').waitFor();const local=kit.frames().find(f=>f.url().includes('/templates/workflow.html'));await local.waitForFunction(()=>window.MoltsetsMotion);await kit.locator('#time').fill('600');await local.waitForFunction(()=>MoltsetsMotion.current===600);
 const localFonts=await local.evaluate(async()=>{await document.fonts.ready;return document.fonts.check('700 64px "Roboto Mono"');});assert(localFonts);
 pass('Offline file:// font load and iframe motion controls');
}finally{await env.close();}
const motionMeta=JSON.parse(await fs.readFile(path.join(output,'motion.json')));assert.equal(motionMeta.frames,120);assert.equal(motionMeta.fps,30);assert.equal(motionMeta.duration,4000);
assert.equal(motionMeta.source.sha256,currentSource.sha256,'Motion export is stale');
assert.equal(JSON.parse(await fs.readFile(path.join(output,'render-source.json'))).source.sha256,currentSource.sha256,'Static export is stale');
const video=path.join(output,'workflow-motion.mp4');assert.equal(crypto.createHash('sha256').update(await fs.readFile(video)).digest('hex'),motionMeta.sha256);
await run(ffmpeg,['-v','error','-i',video,'-f','null','-']);
const {stderr:meta}=await run(ffmpeg,['-i',video,'-f','null','-']);assert(/1920x1080/.test(meta)&&/30 fps/.test(meta)&&/Duration: 00:00:04\.00/.test(meta),meta);
const frames=(await fs.readdir(path.join(output,'motion-frames'))).filter(f=>f.endsWith('.png'));assert.equal(frames.length,120);
const {stdout:alphaBytes}=await run(ffmpeg,['-v','error','-i',path.join(output,'lower-third.png'),'-vf','crop=1:1:0:0,format=rgba','-f','rawvideo','-'],{encoding:'buffer'});assert.equal(alphaBytes[3],0,'Lower third alpha');
pass('Video decodes: 1920 × 1080, 4 seconds, 30 fps, 120 frames; lower-third PNG alpha');
await fs.writeFile(path.join(output,'verification.json'),JSON.stringify({date:new Date().toISOString(),version:tokens.version,checks,contrast:pairs},null,2)+'\n');
console.log(`Verified ${checks.length} groups of requirements.`);
