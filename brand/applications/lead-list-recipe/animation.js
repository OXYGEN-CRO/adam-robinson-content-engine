/* One static DOM, deterministic action, readable hold, controlled reset. */
(() => {
  const duration = 8000, posterMs = 6000;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const $ = selector => document.querySelector(selector);
  const all = selector => [...document.querySelectorAll(selector)];
  const clamp = value => Math.max(0,Math.min(1,value));
  const ease = value => value * value * (3 - 2 * value);
  const progress = (time,start,length) => ease(clamp((time-start)/length));
  const route = $('#progress'), routeLength = route.getTotalLength();
  let frame = null, current = posterMs;
  const ready = Promise.all([document.fonts.ready,...[...document.images].map(image => image.decode())]);
  function seek(ms,{respectReducedMotion=true}={}) {
    current = Math.min(duration,Math.max(0,Number(ms)||0));
    const raw = respectReducedMotion && reduced.matches ? posterMs : current;
    // Reset by returning through the same timeline. The final 120 ms equals the opening.
    const time = raw > 7240 ? 6000 * (1-progress(raw,7240,640)) : raw;
    const filter = progress(time,1120,780), check = progress(time,2850,1000), result = progress(time,4100,720);
    all('.selected').forEach((element,index) => {
      const p = progress(time,350+index*160,260) * (1-progress(time,2200,420));
      element.style.background = `rgba(244,128,93,${p*.16})`;
      element.style.boxShadow = `0 3px 0 rgba(244,128,93,${p})`;
    });
    all('.filter').forEach((element,index) => {
      const p = progress(time,1120+index*210,400);
      element.style.borderColor = p > .5 ? 'var(--ms-brand)' : 'var(--ms-divider)';
      element.style.background = p > .5 ? 'var(--ms-brand-bg)' : 'var(--ms-bg-elevated)';
      element.style.color = p > .5 ? 'var(--ms-fg-primary)' : 'var(--ms-fg-muted)';
      element.style.transform = `translateY(${(1-p)*7}px)`;
    });
    $('#filter-state').style.opacity = filter;
    $('#check-state').style.opacity = check;
    $('#source-check').style.color = check > .5 ? 'var(--ms-fg-secondary)' : 'var(--ms-fg-muted)';
    $('#source-check b').style.opacity = .25+.75*check;
    $('#missing-check b').style.opacity = .25+.75*check;
    $('.result-row').style.transform = `translateY(${(1-result)*42}px)`;
    $('.retained').style.opacity = .25+.75*result;
    $('.sheet-front').style.borderColor = result > .5 ? 'var(--ms-success)' : 'var(--ms-divider)';
    $('.sheet-back').style.transform = `translate(${-12*(1-result)}px,${12*(1-result)}px)`;
    $('.filetype').style.opacity = .35+.65*result;
    const travel = time < 2150 ? .15*progress(time,720,650) : time < 4000 ? .15+.42*progress(time,2150,700) : .57+.43*progress(time,4000,620);
    const point = route.getPointAtLength(travel*routeLength);
    $('#packet').setAttribute('transform',`translate(${point.x} ${point.y})`);
    $('#packet').style.opacity = time >= 4620 ? 0 : progress(time,500,180);
    $('#packet').style.color = time >= 3500 ? 'var(--ms-success)' : 'var(--ms-brand)';
    route.style.strokeDasharray = String(routeLength);
    route.style.strokeDashoffset = String(routeLength*(1-travel));
    route.style.opacity = time < 500 ? 0 : 1;
    $('#seek').value = String(current);
    $('#time').textContent = `${(current/1000).toFixed(2)}s`;
    return current;
  }
  function pause(){if(frame !== null) cancelAnimationFrame(frame);frame=null;}
  function play(){pause();if(reduced.matches){seek(posterMs);return;}const start=performance.now();const tick=now=>{seek(now-start);if(now-start<duration)frame=requestAnimationFrame(tick);else pause();};frame=requestAnimationFrame(tick);}
  $('#play').onclick=play;$('#pause').onclick=pause;$('#poster').onclick=()=>{pause();seek(posterMs);};
  $('#seek').oninput=event=>{pause();seek(event.target.value);};
  reduced.addEventListener('change',()=>{pause();seek(posterMs);});
  window.GraphicMotion={duration,posterMs,ready,seek,pause,play,get current(){return current;}};
  seek(posterMs);
})();
