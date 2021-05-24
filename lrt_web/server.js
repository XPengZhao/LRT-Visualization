var express = require('express');
 var app = express();
 const hostname = '172.21.0.2';
 const port = 8080;
 app.use(express.static('./'));
 app.listen(port, hostname, () => {
  console.log(`Web GUI is running `);
 });
