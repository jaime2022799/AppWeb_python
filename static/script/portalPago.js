var doc = new jsPDF();

const boton = document.getElementById("boton_verificar");



boton.addEventListener('click',function(e) {

    var elementHTML = document.getElementById('contenido').html();

    var specialElementHandlers = {
        '#elementH': function (e, renderer) {
            return true;
        }
    };

    doc.fromHTML(elementHTML, 15, 15, {
        'width': 170,
        'elementHandlers': specialElementHandlers
    });

    // Save the PDF
    doc.save('sample-document.pdf');


    e.preventDefault();


});

