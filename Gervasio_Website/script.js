// To dynamically expand textarea 
var observe;
if (window.attachEvent) {
  observe = function(element, event, handler) {
    element.attachEvent('on' + event, handler);
  };
} else {
  observe = function(element, event, handler) {
    element.addEventListener(event, handler, false);
  };
}
var firstHeight = 0;
var storeH = 0;
var storeH2 = 0;
function init() {
  var text = document.querySelector('textarea');

  function resize() {
    //console.log(text.scrollHeight);
    text.style.height = 'auto';
    if (storeH != text.scrollHeight) {
      text.style.height = text.scrollHeight + 'px';
      storeH = text.scrollHeight;
      if (storeH2 != storeH) {
        console.log("SENT->" + storeH);
        storeH2 = storeH;
      }
    }
  }
  /* 0-timeout to get the already changed text */
  function delayedResize() {
    window.setTimeout(resize, 0);
  }
  observe(text, 'change', resize);
  observe(text, 'cut', delayedResize);
  observe(text, 'paste', delayedResize);
  observe(text, 'drop', delayedResize);
  observe(text, 'keydown', delayedResize);

  text.focus();
  text.select();
  resize();
}
init();


function myFunction() {
  var x = document.querySelector('li');
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}