"use strict";

var _nodemailer = _interopRequireDefault(require("nodemailer"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

var transporter = _nodemailer["default"].createTransport({
  service: "gmail",
  auth: {
    user: "jaimeretamal47@gmail.com",
    pass: "qqfilyrybwadlzpu"
  }
});

var dato = {
  from: "www.blogEvent.cl",
  to: "jaimeretamal47@gmail.com",
  cc: "vincent.s.m.2022@gmail.com",
  subject: "Cotizacion de solicitud eventos",
  text: "Estimado(a) Gusto con saludar, le comunico  la solicitud de contizacion adjunto informacion",
  attachments: [{
    // utf-8 string as an attachment
    filename: 'Cotizacion.xlsx',
    path: './registro.xlsx'
  }]
};
transporter.sendMail(dato, function (error, info) {
  if (error) {
    console.log(error);
  } else {
    console.log('enviado gmail ');
  }
});