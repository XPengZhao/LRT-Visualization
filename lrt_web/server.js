var express = require('express');
 var app = express();
 const hostname = '158.132.255.116';
 const port = 5000;
 app.use(express.static('./dist'));
 app.listen(port, hostname, () => {
  console.log(`Web GUI is running `);
 });
