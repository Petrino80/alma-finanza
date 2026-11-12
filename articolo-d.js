/* Alma Finanza — comportamenti del layout articolo "D": tema chiaro/scuro, barra di avanzamento, indice, copia link. */
(function(){
  var r=document.documentElement;
  function icone(d){var b=document.querySelector('.tgl');if(b)b.textContent=d?'☀️':'🌙'}
  window.toggleTheme=function(){var d=r.classList.toggle('dark');try{localStorage.setItem('alma-theme',d?'dark':'light')}catch(e){}icone(d)};
  icone(r.classList.contains('dark'));
  var bar=document.querySelector('.bar'),art=document.querySelector('.prose');
  if(bar&&art)addEventListener('scroll',function(){var a=art.getBoundingClientRect(),h=a.height-innerHeight*.6;bar.style.width=(Math.min(1,Math.max(0,(-a.top+innerHeight*.2)/h))*100)+'%'},{passive:true});
  var L=document.querySelectorAll('.toc a');
  if(L.length&&'IntersectionObserver'in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)L.forEach(function(x){x.classList.toggle('on',x.getAttribute('href')==='#'+e.target.id)})})},{rootMargin:'-20% 0px -70% 0px'});
    document.querySelectorAll('.prose h2').forEach(function(h){io.observe(h)});
  }
  var c=document.getElementById('copia');
  if(c)c.addEventListener('click',function(){var u=location.href.split('#')[0];(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){c.textContent='Link copiato'}).catch(function(){prompt('Copia il link',u)});setTimeout(function(){c.textContent='Copia link'},2200)});
})();
