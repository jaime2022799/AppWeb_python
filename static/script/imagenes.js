
var fotoMostrada = "/static/img/galeria2.png"
var fotoMostrada1 = "/static/img/galeria2.png"
var fotoMostrada2 = "/static/img/galeria2.png"
var fotoMostrada3 = "/static/img/galeria2.png"
function mostrar(){

    var imagen = document.getElementById('foto')
    var imagen1 = document.getElementById('foto1')
    var imagen2 = document.getElementById('foto2')
    var imagen3 = document.getElementById('foto3')
    //validacion imagen

 
    if (fotoMostrada == '/static/img/galeria2.png'){
        imagen.src = "/static/img/galeria.jpeg";
        fotoMostrada = "/static/img/galeria.jpeg";
    }
    else{
        imagen.src = '/static/img/galeria2.png';
        fotoMostrada = '/static/img/galeria2.png';
    }

    //validacion imagen1

    if(fotoMostrada1 == '/static/img/galeria2.png'){
        imagen1.src = "/static/img/slider.png";
        fotoMostrada1 = "/static/img/slider.png";
    }
    else{
        imagen1.src = '/static/img/galeria2.png';
        fotoMostrada1 = '/static/img/galeria2.png';
    }

    //validacion imagen2
    if(fotoMostrada2 == '/static/img/galeria2.png'){
        imagen2.src = "/static/img/galeria8.jpg";
        fotoMostrada2 = "/static/img/galeria8.jpg";
    }
    else{
        imagen2.src = '/static/img/galeria2.png';
        fotoMostrada2 = '/static/img/galeria2.png';
    }

    //validacion imagen3
    if(fotoMostrada3 == '/static/img/galeria2.png'){
        imagen3.src = "/static/img/galeria6.jpg";
        fotoMostrada3 = "/static/img/galeria6.jpg";
    }
    else{
        imagen3.src = '/static/img/galeria2.png';
        fotoMostrada3 = '/static/img/galeria2.png';
    }


}