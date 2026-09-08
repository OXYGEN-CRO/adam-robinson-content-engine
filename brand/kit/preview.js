// postMessage supports local file previews where browsers isolate iframe origins.
const frame=document.querySelector('iframe');
const send=(action,time)=>frame.contentWindow.postMessage({moltsets:true,action,time},'*');
document.querySelector('#play').addEventListener('click',()=>send('play'));
document.querySelector('#pause').addEventListener('click',()=>send('pause'));
document.querySelector('#time').addEventListener('input',e=>{send('pause');send('seek',Number(e.target.value));document.querySelector('#readout').textContent=(Number(e.target.value)/1000).toFixed(2)+' s';});
addEventListener('message',e=>{if(e.source!==frame.contentWindow||!e.data?.moltsetsTime)return;document.querySelector('#time').value=e.data.time;document.querySelector('#readout').textContent=(e.data.time/1000).toFixed(2)+' s';});
