var collopse_menu_button = false
 function barFunction(e) {
    var x = document.getElementById("menu-links");
    if (!collopse_menu_button){
        x.style.display = 'flex';
        collopse_menu_button = true;
    }else{
        x.style.display = 'none';
        collopse_menu_button = false;
    }
}

var slides = document.querySelectorAll('#slider-box .slides');
var currentSlide = 0;
var previousSlide=0;
var btn_left=document.getElementById('btn-left');
var btn_right=document.getElementById('btn-right');
btn_right.addEventListener("click", nextSlide)
function nextSlide() {
 slides[currentSlide].className = 'slides';
 currentSlide = (currentSlide+1)%slides.length;
 slides[currentSlide].className = 'slides showing';
}

btn_left.addEventListener("click", prevSlide);
function prevSlide() {
    if(currentSlide===0){
     previousSlide=slides.length
 }
    console.log(previousSlide)
 slides[currentSlide].className = 'slides';

 currentSlide = Math.abs((currentSlide-1))%slides.length;
 slides[Math.abs(currentSlide)].className = 'slides showing';
}

$(document).ready(function () {
    var input=document.getElementsByName('quantity')
    for (let i = 0; i <input.length ; i++) {
        input[i].setAttribute('type','hidden')
        input[i].setAttribute('value','1')

    }

});


$('.top-products').slick({
    infinite: true,
    slidesToShow: 6,
    adaptiveHeight: true
});


$('.after-content').slick({
    infinite: true,
    slidesToShow: 6,
    adaptiveHeight: true
});