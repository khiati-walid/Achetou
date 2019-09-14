/********************************************slider for product images*******************************/
var slideIndex =1;
showSlides(slideIndex);
function currentSlide(n) {
  showSlides(slideIndex = n);
}
function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("slide");
  var dots = document.getElementsByClassName("demo");
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
/*****************Tab***************************************************/
var linkIndex =1;
document.getElementById('description').style.display='block';
showTabs(linkIndex);
function currentTab(n) {
  showTabs(linkIndex = n);
}
function showTabs(n) {
  var i;
  var links = document.getElementsByClassName("tablinks");           
  var content = document.getElementsByClassName("tabcontent");
  if (n > content.length) {linkIndex = 1}
  if (n < 1) {linkIndex = content.length}
  for (i = 0; i < content.length; i++) {
    content[i].style.display = "none";
  }

  for (i = 0; i < links.length; i++) {
    links[i].className = links[i].className.replace(" active", "");
  }
  content[linkIndex-1].style.display = "block";
  links[linkIndex-1].className += " active";

}


