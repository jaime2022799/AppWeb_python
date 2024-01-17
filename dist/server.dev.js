"use strict";

var _enviarExcel = require("./enviarExcel");

var Envio_Email = _enviarExcel.excel_send.sendEmail;
router.post('/email', Envio_Email);