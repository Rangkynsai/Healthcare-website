var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}
function open_overlay(){
  document.getElementById("overlay").style.display = 'block';
}
function close_overlay(){
  document.getElementById("overlay").style.display='none';
}
function open_update_overlay(){
  document.getElementById("overlay-feedback").style.display = 'block';
}
function close_update_overlay(){
  document.getElementById("overlay-feedback").style.display='none';
}
function open_overlay1(){
  document.getElementById("overlay-order").style.display = 'block';
}
function close_overlay1(){
  document.getElementById("overlay-order").style.display='none';
}
