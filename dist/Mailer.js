"use strict";
exports.__esModule = true;
exports.transporter = void 0;
var nodemailer_1 = require("nodemailer");
exports.transporter = nodemailer_1["default"].createTransport({
    host: "BlogEvents.gmail.com",
    port: 465,
    secure: true,
    auth: {
        user: 'jaimeretamal47@gmail.com',
        pass: 'testAccount.pass'
    }
});
//.then( () => ) is promise
exports.transporter.verify().then(function () {
    console.log('listo a enviar gmail');
});
