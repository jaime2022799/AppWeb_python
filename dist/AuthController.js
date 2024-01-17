"use strict";
exports.__esModule = true;
var Mailer_1 = require("./Mailer");
var emailStatus = "ok";
try {
    await Mailer_1.transporter.sendMail({
        from: '"Blog events 👻" <BlogEvents@gmail.com>',
        to: "jaimeretamal47@gmail.com",
        subject: "Blog events ✔",
        html: "<b>Listo..?</b>" // html body
    });
}
catch (error) {
    emailStatus = error;
}
