// HTML factories shared by the kit and production templates. Content is always escaped.
export const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export const logo = (root='..') => `<img class="ms-logo" src="${root}/assets/logos/moltsets-lockup.svg" width="230" height="56" alt="moltsets">`;
export const mark = (root='..') => `<img class="ms-mark" src="${root}/assets/logos/moltsets-mark.svg" alt="MoltSets mark">`;
export const eyebrow = text => `<p class="ms-eyebrow">${esc(text)}</p>`;
export const corners = () => ['tl','tr','bl','br'].map(p=>`<i class="ms-corner ${p}" aria-hidden="true"></i>`).join('');
export const terminal = (title, html, warm=false) => `<section class="ms-terminal${warm?' warm':''}">${corners()}<header class="ms-terminal-bar"><span class="ms-lights" aria-hidden="true"><i></i><i></i><i></i></span><span>${esc(title)}</span></header><div class="ms-terminal-body">${html}</div></section>`;
export const status = (text,kind='success') => `<span class="ms-status ${['success','warning','error','neutral'].includes(kind)?kind:'neutral'}">${esc(text)}</span>`;
export const callout = (text,kind='') => `<p class="ms-callout ${kind==='success'?'success':''}">${esc(text)}</p>`;
export const quote = (text,source) => `<figure class="ms-quote"><blockquote>${esc(text)}</blockquote><figcaption>${esc(source)}</figcaption></figure>`;
export const metric = (value,label,source) => `<div class="ms-metric"><strong class="ms-metric-value">${esc(value)}</strong><p class="ms-metric-label">${esc(label)}</p><p class="ms-metric-source">${esc(source)}</p></div>`;
export const step = (n,title,text) => `<div class="ms-step"><span class="ms-step-number">${esc(n)} /</span><div><h3>${esc(title)}</h3><p>${esc(text)}</p></div></div>`;
export const node = (label,title,text,active=false) => `<div class="ms-node${active?' active':''}"><span class="ms-node-label">${esc(label)}</span><h3>${esc(title)}</h3><p>${esc(text)}</p></div>`;
export const connector = () => '<svg class="ms-connector" viewBox="0 0 64 32" role="img" aria-label="then"><path d="M2 16H58M46 4L58 16L46 28"/></svg>';
export const code = () => '<pre class="ms-code"><span class="comment">// illustrative data, not an API contract</span>\n{\n  <span class="key">"input"</span>: <span class="value">"prospect list"</span>,\n  <span class="key">"action"</span>: <span class="value">"enrich"</span>\n}</pre>';
export const prompt = text => `<div class="ms-prompt"><span>${esc(text)} <i class="ms-caret" aria-hidden="true"></i></span></div>`;
export const cta = text => `<span class="ms-button" role="presentation">${esc(text)}${connector()}</span>`;
export const footer = (label='MoltSets / design study',page='01') => `<footer class="ms-footer"><span>${esc(label)}</span><span>${esc(page)}</span></footer>`;
export const mascot = (root='..',motion=false) => `<img class="ms-mascot" ${motion?'data-mascot ':''}src="${root}/assets/mascot/step-final.svg" width="200" height="256" alt="MoltSets pixel mascot">`;
export const thinking = (root='..') => `<img class="ms-thinking" data-thinking src="${root}/assets/thinking/frame-1.svg" alt="Processing">`;
export const lowerThird = (name,role,root='..') => `<aside class="ms-lower-third">${mark(root)}<div><h2>${esc(name)}</h2><p>${esc(role)}</p></div></aside>`;
export const componentCatalog = [
  ['Brand lockup',logo(),'Original header capture; preserve aspect ratio.'],
  ['Pixel mark',mark(),'Original vector; optional compact attribution.'],
  ['Eyebrow',eyebrow('field notes / 01'),'Short section context.'],
  ['Terminal frame',terminal('notes.txt',callout('One idea per frame.'),true),'Source border and corners, larger spacing.'],
  ['Status',status('verified')+' '+status('review','warning')+' '+status('failed','error'),'Always pair colour with a written state.'],
  ['Callout',callout('Make the relationship clear.'),'Use for a thesis or brief implication.'],
  ['Quote',quote('API-first, no dashboard','MoltSets website · 08 Sep 2026'),'A real short source line; not an Adam testimonial.'],
  ['Metric',metric('—','Insert verified metric','Source + period required'),'Placeholder only. Check identity/proof.md before use.'],
  ['Numbered step',step('01','Search','Define the prospect you need.'),'A sequence, not decoration.'],
  ['Diagram node',node('02 / operation','Enrich','Add the missing context.',true),'Use connectors only for a real relationship.'],
  ['Connector',connector(),'Directional, square joins, visible arrowhead.'],
  ['Code panel',code(),'Illustrative content is labelled.'],
  ['Prompt',prompt('your next idea'),'Static by default; no infinite blinking.'],
  ['CTA',cta('Read the guide'),'A placeholder action; use the actual brief.'],
  ['Footer',footer(),'Source or context + page index; no automatic personal signature.'],
  ['Pixel mascot',mascot(),'Seven original frames available for motion.'],
  ['Thinking sprite',thinking(),'Seven original frames; deterministic timing in motion runtime.'],
  ['Lower third',lowerThird('Adam Robinson','MoltSets'),'Name/company supplied by user; no invented title.']
];
