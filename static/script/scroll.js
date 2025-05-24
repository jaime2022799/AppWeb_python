
window.addEventListener("scroll", function(){

    //header
    var header = document.querySelector("header");
  
    header.classList.toggle('sticky', window.scrollY > 0);
   

});

