'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/', express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/myhtml.html');
});

app.get('/hello', (req, res) => {
  res.json({
    message: "Hello World!"
  })
});

app.listen(8080);