//import {blobToBase64} from './blobManager.js';
//import {file} from './blobManager.js';




/*
function sendemail() {

   Email.send({
      Host : "smtp.elasticemail.com",
      Username : "jaimeretamal47@gmail.com",
      Password : "0859758872E4A0D9D5C00698BF545B869E9F",
      To : 'jaimeretamal47@gmail.com',
      From : "jaimeretamal47@gamil.com",
      Subject : "This is the subject",
      Body : "And this is the body"
  }).then(
    message => alert(message)
  );
  
}
*/

const enviar_excel = document.getElementById("enviar");
const tabla_file = document.getElementById("tabla");

/*
function uploadFileToServer()
{
  var file = event.srcElement.files[0];
   var reader = new FileReader();
   reader.readAsBinaryString(file);
   reader.onload = function () {
       var dataUri = "data:" + file.type + ";base64," + btoa(reader.result);
       Email.send({
           SecureToken : "********",
           To : 'info@destination.com',
           From : "you@source.com",
           Subject : "Send with base64 attachment",
           Body : "Sending file:" + file.name,
           Attachments : [
          	{
          		name : file.name,
          		data : dataUri
          	}]
       }).then(
         message => alert(message)
       );
   };
   reader.onerror = function() {
       console.log('there are some problems');
   };
}*/

enviar_excel.addEventListener('click',  function(event) {

   

   var recibe_archivo = document.getElementById("tabla").files;
   console.log(recibe_archivo);

   
   if(recibe_archivo.length > 0){
    var cargarimagen =  recibe_archivo[0];
    console.log(cargarimagen);
   }

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
      SecureToken : "6835a161-ebee-40b3-adc3-5f16e949ad43",
      To : 'jaimeretamal47@gmail.com, mendozajaiser54@gmail.com',
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
    
    /*var nueva_imagen = document.createElement('img');
    nueva_imagen.src = imagenBase64;
    
    document.getElementById("imagen").innerHTML = nueva_imagen.outerHTML;*/


   }


  
   reader.readAsDataURL(cargarimagen);
    


    event.preventDefault();

});




