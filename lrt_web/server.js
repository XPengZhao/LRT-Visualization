var express = require('express');
 var app = express();
 const hostname = 'localhost';
 const port = 3000;
 app.use(express.static('./'));
 app.listen(port, hostname, () => {
  console.log(`web gui is running `);
 });
