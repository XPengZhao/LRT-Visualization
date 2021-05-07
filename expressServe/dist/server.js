var express = require('express');
 var app = express();
 const hostname = '172.21.0.2';
 const port = 80;
 app.use(express.static('./'));
 app.listen(port, hostname, () => {
  console.log(`comp5322 Server is running `);
 });
