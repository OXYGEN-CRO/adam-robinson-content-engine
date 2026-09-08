import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {environment, glyphFonts} from '../../brand/browser.mjs';
const repo=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const dir=path.join(repo,'output/rb2b-operating-map');
const svg=await fs.readFile(path.join(dir,'rb2b-operating-map.svg'),'utf8');
const env=await environment();
try {
 const page=await env.browser.newPage({viewport:{width:3600,height:7560},deviceScaleFactor:1});
 await page.setContent('<!doctype html><html><head><meta charset="UTF-8"><style>body{margin:0;background:#0A0B0E}svg{display:block}</style></head><body>'+svg+'</body></html>');
 await page.evaluate(()=>document.fonts.ready);
 const fonts=await glyphFonts(page,'svg text');
 const geometry=await page.evaluate(()=>{
   const issues=[];const rects=[];
   for(const t of document.querySelectorAll('svg text')){
     const b=t.getBBox();const parent=t.parentElement;
     if(b.x<0||b.y<0||b.x+b.width>3600||b.y+b.height>7560)issues.push({kind:'canvas',text:t.textContent,b});
     if(t.dataset.right&&b.x+b.width>Number(t.dataset.right)+2)issues.push({kind:'width',text:t.textContent,right:b.x+b.width,limit:t.dataset.right});
     rects.push({text:t.textContent,x:b.x,y:b.y,w:b.width,h:b.height});
   }
   for(let i=0;i<rects.length;i++)for(let j=i+1;j<rects.length;j++){
     const a=rects[i],b=rects[j];const ix=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x);const iy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
     if(ix>3&&iy>3)issues.push({kind:'text-overlap',a:a.text,b:b.text,ix,iy});
   }
   return {issues,textCount:rects.length,links:[...document.querySelectorAll('svg a')].map(a=>a.getAttribute('href'))};
 });
 await page.screenshot({path:path.join(dir,'rb2b-operating-map.png'),fullPage:true});
 const crops=[
 ['01-company-structure',0,610,3600,1280],
 ['02-acquisition-channels',0,1890,3600,1775],
 ['03-product-and-revenue-funnel',0,3710,3600,1025],
 ['04-engineering-and-infrastructure',0,4780,3600,1220],
 ['05-fin-support-and-feedback',0,6060,3600,1102],
 ['06-evidence-and-limits',0,7162,3600,398],
 ];
 for(const [name,x,y,width,height] of crops)await page.screenshot({path:path.join(dir,'details',name+'.png'),clip:{x,y,width,height}});
 await fs.writeFile(path.join(dir,'render-review.json'),JSON.stringify({fonts,...geometry,dimensions:[3600,7560],crops},null,2));
 console.log(JSON.stringify({fonts,issues:geometry.issues,textCount:geometry.textCount,links:geometry.links.length}));
}finally{await env.close()}
