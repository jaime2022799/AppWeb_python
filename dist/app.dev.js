"use strict";

var express = require('express');

var bodyparser = require('body-parser');

var path = require('path');

var app = express();
app.use(express.json());
app.use(express.urlencoded({
  extended: true
}));
app.use(bodyparser.urlencoded({
  extended: true
}));
app.use(express["static"]('public'));
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'html'); //app.set('public engine','ejs');
//app.set('public',express.static(__dirname + '/public'));

app.use("/", require("./routes"));
var PORT = process.env.PORT || 8080;
app.listen(PORT, function () {
  console.log("server started on port 8080", PORT);
});