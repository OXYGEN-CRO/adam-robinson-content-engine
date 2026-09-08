/* Browser global deliberately works over file://. Deterministic seek is the export API. */
(() => {
  const tokens=window.MoltsetsTokens.motion;
  const duration=tokens.duration;
  const reduced=matchMedia('(prefers-reduced-motion: reduce)');
  const clamp=v=>Math.min(1,Math.max(0,v));
  let frame=null, current=duration;
  const assetRoot=new URL('../assets/',document.currentScript.src);
  const mascotNames=[1,2,3,4,5,6,'final'];
  // Decode every frame before exports; no network is needed.
  const ready=Promise.all([...mascotNames.map(n=>`mascot/step-${n}.svg`),...[1,2,3,4,5,6,7].map(n=>`thinking/frame-${n}.svg`)].map(path=>{const i=new Image();i.src=new URL(path,assetRoot);return i.decode();}));
  // Cubic bezier evaluated by time (binary solve x), shared with token curve.
  function ease(t) {
    const [x1,y1,x2,y2]=tokens.ease;
    const cubic=(u,a,b)=>3*(1-u)**2*u*a+3*(1-u)*u*u*b+u**3;
    let lo=0,hi=1,u=t;
    for(let i=0;i<18;i++){u=(lo+hi)/2;if(cubic(u,x1,x2)<t)lo=u;else hi=u;}
    return cubic(u,y1,y2);
  }
  function seek(ms,{respectReducedMotion=true}={}) {
    current=Math.max(0,Math.min(duration,Number(ms)||0));
    const time=respectReducedMotion&&reduced.matches?duration:current;
    document.querySelectorAll('[data-enter]').forEach(el=>{
      const start=Number(el.dataset.enter)||0, length=Number(el.dataset.duration)||tokens.enter;
      const p=clamp((time-start)/length), e=ease(p);
      el.style.opacity=String(p===0?0:p===1?1:e);
      el.style.transform=`translateY(${(1-e)*tokens.distance}px)`;
    });
    document.querySelectorAll('[data-draw]').forEach(el=>{
      const length=el.getTotalLength(),p=clamp((time-Number(el.dataset.draw))/tokens.enter);
      el.style.strokeDasharray=String(length);el.style.strokeDashoffset=String(length*(1-ease(p)));
    });
    let mi=0;tokens.mascotTimes.forEach((t,i)=>{if(time>=t)mi=i;});
    document.querySelectorAll('[data-mascot]').forEach(el=>el.src=new URL(`mascot/step-${mascotNames[mi]}.svg`,assetRoot));
    const cycle=tokens.thinkingHolds.reduce((a,b)=>a+b,0);let position=time%cycle,ti=0;
    for(let i=0;i<tokens.thinkingHolds.length;i++){if(position<tokens.thinkingHolds[i]){ti=i;break;}position-=tokens.thinkingHolds[i];}
    if(time===duration)ti=0;
    document.querySelectorAll('[data-thinking]').forEach(el=>el.src=new URL(`thinking/frame-${ti+1}.svg`,assetRoot));
    document.querySelectorAll('[data-time]').forEach(el=>el.textContent=(current/1000).toFixed(2)+' s');
    document.querySelectorAll('[data-seek]').forEach(el=>el.value=String(current));
    if(window.parent!==window)window.parent.postMessage({moltsetsTime:true,time:current},'*');
    return current;
  }
  function pause(){if(frame!==null)cancelAnimationFrame(frame);frame=null;document.querySelectorAll('[data-play]').forEach(b=>b.textContent='Replay');}
  function play(){pause();if(reduced.matches){seek(duration);return;}const start=performance.now();const tick=now=>{seek(now-start);if(now-start<duration)frame=requestAnimationFrame(tick);else pause();};frame=requestAnimationFrame(tick);document.querySelectorAll('[data-play]').forEach(b=>b.textContent='Playing');}
  document.querySelectorAll('[data-play]').forEach(b=>b.addEventListener('click',play));
  document.querySelectorAll('[data-pause]').forEach(b=>b.addEventListener('click',pause));
  document.querySelectorAll('[data-seek]').forEach(el=>el.addEventListener('input',()=>{pause();seek(el.value);}));
  reduced.addEventListener('change',()=>{pause();seek(duration);});
  window.MoltsetsMotion={duration,seek,pause,play,ready,get current(){return current;}};
  addEventListener('message',event=>{
    if(event.source!==window.parent||!event.data?.moltsets)return;
    const {action,time}=event.data;
    if(action==='play')play();
    if(action==='pause')pause();
    if(action==='seek')seek(time);
  });
  seek(duration);
})();
