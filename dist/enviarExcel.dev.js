"use strict";

var _module = require("./module");

//import Swal from 'sweetalert';
//const nodemailer = require("nodemailer");
//const { default: swal } = require("sweetalert");
//const nodemailer = require('nodemailer');

/*let transporter = nodemailer.createTransport({
   service: "gmail",
   auth: {
      user: "jaimeretamal47@gmail.com",
      pass: "qqfilyrybwadlzpu"

   

   }

});  
*/
var excel_send = document.getElementById('enviar');
excel_send.addEventListener('click', function () {
  var check = true;

  if (check == false) {
    swal("algo salio mal", "reintentar...", "warning");
  } else {
    swal("redireccionado al contador(a)", "enviado", "success");
  }
});
/*
transporter.sendMail({
    from: "www.blogEvent.cl",
  to: "jaimeretamal47@gmail.com",
  cc: "vincent.s.m.2022@gmail.com",
  subject: "Cotizacion de solicitud eventos",
  text: "Estimado(a) Gusto con saludar, le comunico  la solicitud de contizacion adjunto informacion",
    attachments:[
     {   // utf-8 string as an attachment
         filename: 'Cotizacion.xlsx',
         path: './registro.xlsx'
     }
  ]
})
 transporter.verify().then(console.log).catch(console.error);
 */

/*
let transporter = nodemailer.createTransport({
   service: "gmail",
   auth: {
      user: "jaimeretamal47@gmail.com",
      pass: "qqfilyrybwadlzpu"
     
     }
});   


let dato = {
   from: "www.blogEvent.cl",
   to: "jaimeretamal47@gmail.com",
   cc: "vincent.s.m.2022@gmail.com",
   subject: "Cotizacion de solicitud eventos",
   text: "Estimado(a) Gusto con saludar, le comunico  la solicitud de contizacion adjunto informacion",
     attachments:[
      {   // utf-8 string as an attachment
          filename: 'Cotizacion.xlsx',
          path: './registro.xlsx'
      }
   ]
}

transporter.sendMail(dato, function(error, info){
   if (error) {
     console.log(error);
   } else {
     console.log('Email sent: ' + info.response);
   }
 });

*/

/*
transporter.post("/send", (req, res) => {
     let send_csv = new multiparty.Form();
   let data = {};
     form.parse(req, function (err, fields) {
      console.log(fields);
      Object.keys(fields).forEach(function (property) {
         data[property] = fields[property].toString();
      });

      let details = {
         from: "www.blogEvent.cl",
         to: "jaim.retamal@duocuc.cl",
         cc: "jaimeretamal47@gmail.com",
         subject: "Cotizacion de solicitud eventos",
         text: "estimado gusto con saludar , esperando que se encuentre bien se adjunta excel de cotizacion de eventos. Saludos",
      
         attachments:[
            {   // utf-8 string as an attachment
                filename: 'Cotizacion.xlsx',
                path: './registro.xlsx'
            }
      
            
        ]
      };
        transporter.sendMail(details, (err, data) => {
         if (err) {
            console.log(err);
            res.status(500).send("Something went wrong.");
         }else {
            res.status(200).send("email succesfully");
         }
      })
   })
})
*/
//});