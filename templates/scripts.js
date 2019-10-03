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



var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("slides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";
}


$('.top-products').slick({
    infinite: true,
    slidesToShow: 3
});