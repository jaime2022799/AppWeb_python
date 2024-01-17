"use strict";

var app = express();

var path = require('path');

var router = Router();

var _require = require('express'),
    Router = _require.Router;

app.use(require('./router.js'));
app.use(express["static"](path.join(__dirname, 'public')));
app.listen(3000, function () {
  console.log('server local 3000');
});
module.exports = router;