'use strict';

const express = require('express');

const app = express();

app.use('/assets', express.static('assets'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

app.get('/doubling', (req, res) => {
  if (req.query.input === undefined) {
    res.json({
      "error": "Please provide an input!"
    })
  } else if (req.query.input) {
    res.json({
      "received": req.query.input,
      "result": req.query.input * 2,
    })
  }
})

app.listen(8080);