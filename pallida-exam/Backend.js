'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/', express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/Index.html');
});

let newLicencePlate = { platenumber: 'here will be the plate number'};

app.get('/search', (req, res) => {
  res.json(newLicencePlate);
});

app.post('/search', (req, res) => {
  console.log(req.body);
  newLicencePlate = { 'platenumber': req.body.platenumber };
  res.json(newLicencePlate);
});

app.listen(8000);