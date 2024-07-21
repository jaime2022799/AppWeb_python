
const boton = document.getElementById("boton_verificar");

boton.addEventListener("click", function(e) {


        const { jsPDF } = window.jspdf;
    
       // let doc = new jsPDF('1', 'mm',[1500, 1400]);
        
        //let pdfjs = document.getElementById('contenido');
        
        //convert pdf a base64 string

        //convert pdf to string
         
        /*var pdf = doc.html(pdfjs, {
            callback: function(doc) {
                doc.save("factura.pdf");
    
            },
            x: 12,
            y: 12
        });*/

        
        var pdf = new jsPDF('p', 'pt', [1400, 1300]);

        pdf.html(document.getElementById('contenido'), {
        callback: function (pdf) {
        // example text
        //pdf.text(20, 20, 'Hello world!');
        //pdf.text(20, 30, 'This is client-side Javascript, pumping out a PDF.');

        var base = pdf.output('datauri'); // directly to base664

        console.log("base64 is  ");
        console.log(base);

        // you can generate in another format also  like blob
            var out = pdf.output('blob');
        var reader = new FileReader();

        reader.readAsDataURL(out); 
        reader.onloadend = function() { // for blob to base64
                base64data = reader.result; 
                console.log("base64 data is ");               
                console.log(base64data );
        }
        pdf.save('factura.pdf');

        Email.send({
            SecureToken : "167af3e5-f3ee-4342-86ad-e431aebe2b29",
            To : 'jaimeretamal47@gmail.com',
            From : "jaimeretamal47@gmail.com",
            Subject : "Facturacion 2024",
            Body : "Estimado(a) se a enviado una solicitud al departamento de Factura digital,   se comunicaran con usted mediante los datos solicitados",
            
            Attachments : [
                {
                   name : "Factura.pdf",
                   data : base
                   
                }]
            
         }).then(
            
          //message => alert(message)
          message => swal('Genial...','se a enviado una notificacion de su Factura','success')
        );
            

        }
        })  
        
        //var pdfBase64 = pdf.output('datauristring')
        // btoa(pdf.output());

        //var pdf2 = btoa(pdf.output('datauristring'))

       

    //console.log(pdfBase64)
    //var x = 'newpdf.pdf';
    //base64 = x.toString();
    
    /*Email.send({
        SecureToken : "167af3e5-f3ee-4342-86ad-e431aebe2b29",
        To : 'jaimeretamal47@gmail.com',
        From : "jaimeretamal47@gmail.com",
        Subject : "Facturacion 2024",
        Body : "Estimado(a) se a enviado una solicitud al departamento de Factura digital,   se comunicaran con usted mediante los datos solicitados",
        
        Attachments : [
            {
               name : "Factura.pdf",
               data : base
               
            }]
        
     }).then(
        
      //message => alert(message)
      message => swal('Genial...','se a enviado una notificacion de su Factura','success')
    );
    
     
    
    */

    e.preventDefault();
    


})

/*
var pdf = new jsPDF('p', 'pt', 'a4');

 pdf.html(document.getElementById('contenido'), {
    callback: function (pdf) {

    // example text
    pdf.text(20, 20, 'Hello world!');
    pdf.text(20, 30, 'This is client-side Javascript, pumping out a PDF.');

    var base = pdf.output('datauri'); // directly to base664

    console.log("base64 is  ");
    console.log(base);

    // you can generate in another format also  like blob
     var out = pdf.output('blob');
    var reader = new FileReader();

    reader.readAsDataURL(out); 
    reader.onloadend = function() { // for blob to base64
         base64data = reader.result; 
         console.log("base64 data is ");               
         console.log(base64data );
    }
    pdf.save('factura.pdf');

    }
    })  

*/



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


