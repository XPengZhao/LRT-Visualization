var express = require('express');
 var app = express();
 const hostname = '10.11.45.210';
 const port = 8080;
 app.use(express.static('./'));
 app.listen(port, hostname, () => {
  console.log(`web gui is running `);
 });
