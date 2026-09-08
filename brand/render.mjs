import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {spawn} from 'node:child_process';
import ffmpeg from 'ffmpeg-static';
import {environment,root,output,settle,glyphFonts,textBounds,sourceDigest} from './browser.mjs';
const manifest=JSON.parse(await fs.readFile(path.join(root,'templates/manifest.json')));
const tokens=JSON.parse(await fs.readFile(path.join(root,'tokens.json')));
await fs.mkdir(output,{recursive:true});
const env=await environment();
const inputs=await sourceDigest();
try{
 if(process.argv[2]==='motion'){
  const scene=manifest.find(s=>s.id==='workflow');const frames=path.join(output,'motion-frames');await fs.mkdir(frames,{recursive:true});
  const page=await env.browser.newPage({viewport:{width:scene.width,height:scene.height},deviceScaleFactor:1});await page.goto(`${env.base}/${scene.file}`);await settle(page);
  const count=Math.round(tokens.motion.duration/1000*tokens.motion.fps);
  for(let i=0;i<count;i++){
   await page.evaluate(ms=>MoltsetsMotion.seek(ms,{respectReducedMotion:false}),i*1000/tokens.motion.fps);
   await page.screenshot({path:path.join(frames,`${String(i).padStart(4,'0')}.png`),animations:'disabled'});
   if(i%30===0)console.log(`Motion: frame ${i}/${count}`);
  }
  await new Promise((resolve,reject)=>{const p=spawn(ffmpeg,['-y','-framerate',String(tokens.motion.fps),'-i',path.join(frames,'%04d.png'),'-frames:v',String(count),'-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-movflags','+faststart',path.join(output,'workflow-motion.mp4')],{stdio:['ignore','ignore','pipe']});let error='';p.stderr.on('data',s=>error+=s);p.on('error',reject);p.on('close',code=>code===0?resolve():reject(new Error(error)));});
  await fs.writeFile(path.join(output,'motion.json'),JSON.stringify({template:scene.id,dimensions:[scene.width,scene.height],fps:tokens.motion.fps,frames:count,duration:tokens.motion.duration,version:tokens.version,source:inputs,sha256:crypto.createHash('sha256').update(await fs.readFile(path.join(output,'workflow-motion.mp4'))).digest('hex')},null,2));
  console.log('Rendered workflow-motion.mp4 and deterministic PNG sequence.');
 }else{
  const report=[];
  for(const s of manifest){
   const page=await env.browser.newPage({viewport:{width:s.width,height:s.height},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`);});
   await page.goto(`${env.base}/${s.file}`);await settle(page);
   const bounds=await textBounds(page);const fonts=await glyphFonts(page,'.ms-art');
   await page.screenshot({path:path.join(output,s.id+'.png'),omitBackground:s.transparent});
   const scale=360/s.width;await page.setViewportSize({width:360,height:Math.ceil(s.height*scale)});await page.addStyleTag({content:`.ms-art{transform:scale(${scale});transform-origin:top left;}body{width:360px;height:${Math.ceil(s.height*scale)}px;overflow:hidden;}`});
   await page.screenshot({path:path.join(output,s.id+'-phone.png'),omitBackground:s.transparent});
   report.push({id:s.id,dimensions:[s.width,s.height],fonts,bounds,errors});await page.close();console.log(`Rendered ${s.id}`);
  }
  const components=JSON.parse(await fs.readFile(path.join(root,'components-manifest.json')));await fs.mkdir(path.join(output,'components'),{recursive:true});
  for(const s of components){const page=await env.browser.newPage({viewport:{width:s.width,height:s.height}});await page.goto(`${env.base}/${s.file}`);await settle(page);const bounds=await textBounds(page,'.component-canvas');await page.screenshot({path:path.join(output,'components',s.id+'.png')});report.push({id:'component/'+s.id,bounds});await page.close();}
  const kit=await env.browser.newPage({viewport:{width:1440,height:1000}});await kit.goto(`${env.base}/kit/index.html`);await settle(kit);await kit.screenshot({path:path.join(output,'kit-overview.png')});await kit.locator('#components').screenshot({path:path.join(output,'kit-components.png')});await kit.screenshot({path:path.join(output,'kit-full.png'),fullPage:true});await kit.setViewportSize({width:390,height:844});await kit.evaluate(()=>scrollTo({top:0,behavior:'instant'}));await kit.screenshot({path:path.join(output,'kit-phone.png')});
  await fs.writeFile(path.join(output,'render-report.json'),JSON.stringify(report,null,2)+'\n');
  await fs.writeFile(path.join(output,'render-source.json'),JSON.stringify({version:tokens.version,source:inputs},null,2)+'\n');
  if(report.some(r=>r.bounds?.length||r.errors?.length))throw new Error('Render problems; inspect output/moltsets-brand/render-report.json');
  console.log('Rendered all templates, phone previews, component samples, and kit.');
 }
}finally{await env.close();}
