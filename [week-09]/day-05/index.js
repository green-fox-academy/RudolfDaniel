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
    message: "Thank you for your attention!"
  })
});

app.listen(8080);
