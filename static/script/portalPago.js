
const boton = document.getElementById("boton_verificar");

boton.addEventListener("click", function(e) {

    
    const { jsPDF } = window.jspdf;
    
    let doc = new jsPDF('1', 'mm',[1500, 1400]);
    let pdfjs = document.getElementById('contenido');

    doc.html(pdfjs, {
        callback: function(doc) {
            doc.save("Factura_Cotizacion.pdf");

        },
        x: 12,
        y: 12
    });


    e.preventDefault();
})


/*


   //convercion de base64 a string

   const reader = new FileReader();

   
   reader.onload = function(recibe_archivo) {

    var imagenBase64 = recibe_archivo.target.result;

    const base64 = imagenBase64.toString();
    
    const x = base64;
    var encodig_64 = btoa(x);

    console.log(encodig_64);
    
    console.log(imagenBase64);
   
    Email.send({
      SecureToken : "a6d0a20e-d612-498b-82a6-23a6a2203efc",
      To : 'jaimeretamal47@gmail.com',
      From : "jaimeretamal47@gmail.com",
      Subject : "Cotizacion 2024",
      Body : "Estimado(a) se a enviado una solicitud al departamento de cotizadores,   se comunicaran con usted mediante los datos solicitados",
      
      
      Attachments : [
         {
            name : "CotizacionJaime.xlsx",
            data : imagenBase64
            
         }]
         
      
   }).then(
      
    //message => alert(message)
    message => swal('Genial...','se a enviado una notificacion de su cotizacion','success')
  );


  reader.onerror = function() {
   console.log(reader.error);
 };


*/


