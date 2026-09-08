import http from 'node:http';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {chromium} from 'playwright';
import crypto from 'node:crypto';
export const root=path.dirname(fileURLToPath(import.meta.url));
export const output=path.resolve(root,'../output/moltsets-brand');
export async function sourceDigest(){
 const files=['tokens.json','tokens.css','tokens.js','base.css','components.css','components.mjs','templates/scenes.mjs','templates/compositions.css','motion/runtime.js','motion/motion.css','render.mjs','browser.mjs'];
 async function collect(dir){for(const entry of await fs.readdir(path.join(root,dir),{withFileTypes:true})){const name=dir+'/'+entry.name;if(entry.isDirectory())await collect(name);else files.push(name);}}
 await collect('assets');
 const hash=crypto.createHash('sha256');for(const name of files.sort()){hash.update(name+'\0');hash.update(await fs.readFile(path.join(root,name)));}
 return {sha256:hash.digest('hex'),files:files.sort()};
}
export async function environment(){
 const mime={'.html':'text/html','.css':'text/css','.js':'text/javascript','.json':'application/json','.svg':'image/svg+xml','.png':'image/png','.ttf':'font/ttf'};
 const server=http.createServer(async(req,res)=>{
  try{const name=decodeURIComponent(new URL(req.url,'http://local').pathname);const file=path.resolve(root,'.'+name);if(!file.startsWith(root+path.sep))throw new Error('Outside brand');const bytes=await fs.readFile(file);res.writeHead(200,{'Content-Type':mime[path.extname(file)]||'application/octet-stream'});res.end(bytes);}
  catch{res.writeHead(404);res.end('Not found');}
 });
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true});
 return {browser,base:`http://127.0.0.1:${server.address().port}`,close:async()=>{await browser.close();await new Promise(resolve=>server.close(resolve));}};
}
export async function settle(page){
 await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode()));if(window.MoltsetsMotion){await MoltsetsMotion.ready;MoltsetsMotion.pause();MoltsetsMotion.seek(MoltsetsMotion.duration);}});
}
export async function glyphFonts(page,selector){
 const session=await page.context().newCDPSession(page);await session.send('DOM.enable');await session.send('CSS.enable');
 const {root:doc}=await session.send('DOM.getDocument');const {nodeIds}=await session.send('DOM.querySelectorAll',{nodeId:doc.nodeId,selector:`${selector}, ${selector} *`});
 // CDP reports direct text children, so inspect the entire subtree explicitly.
 const results=await Promise.all(nodeIds.map(nodeId=>session.send('CSS.getPlatformFontsForNode',{nodeId})));
 const combined=new Map();for(const result of results)for(const f of result.fonts){const key=f.postScriptName+'|'+f.isCustomFont;const existing=combined.get(key);if(existing)existing.glyphCount+=f.glyphCount;else combined.set(key,{...f});}
 await session.detach();return [...combined.values()];
}
export async function textBounds(page,canvas='.ms-art'){
 return page.evaluate(selector=>{
  const art=document.querySelector(selector);const outer=art.getBoundingClientRect();const problems=[];const walker=document.createTreeWalker(art,NodeFilter.SHOW_TEXT);let n;
  while(n=walker.nextNode()){
   if(!n.textContent.trim()||['SCRIPT','STYLE','TITLE'].includes(n.parentElement.tagName))continue;
   const range=document.createRange();range.selectNodeContents(n);const rects=[...range.getClientRects()];
   for(const r of rects){if(!r.width||!r.height)continue;if(r.left<outer.left-2||r.right>outer.right+2||r.top<outer.top-2||r.bottom>outer.bottom+2)problems.push({text:n.textContent.trim(),reason:'outside canvas'});
    let parent=n.parentElement;while(parent&&parent!==art){const c=getComputedStyle(parent);if(['hidden','clip'].includes(c.overflowX)||['hidden','clip'].includes(c.overflowY)){const p=parent.getBoundingClientRect();if(r.left<p.left-2||r.right>p.right+2||r.top<p.top-2||r.bottom>p.bottom+2)problems.push({text:n.textContent.trim(),reason:'clipped by '+parent.className});}parent=parent.parentElement;}
   }
  }
  return problems;
 },canvas);
}
