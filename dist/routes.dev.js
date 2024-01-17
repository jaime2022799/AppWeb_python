"use strict";

var router = require("express").Router();

var correoNotificacion = require('./enviarExcel.js');

router.route("/").get(function (req, res) {
  //var correoEmail = "jaimeretamal47@gmail.com";
  //correoNotificacion(correoEmail);
  res.render("index");
});
module.exports = router;