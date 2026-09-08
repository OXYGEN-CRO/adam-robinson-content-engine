const observer=new ResizeObserver(entries=>entries.forEach(({target,contentRect})=>target.style.setProperty('--preview-scale',contentRect.width/Number(target.dataset.width))));
document.querySelectorAll('.preview').forEach(el=>observer.observe(el));
