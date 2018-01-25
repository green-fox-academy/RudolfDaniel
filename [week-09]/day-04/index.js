'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/assets', express.static('assets'));
app.use(bodyParser.json());

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

app.get('/greeter', (req, res) => {
  const name = req.query.name;
  const title = req.query.title;
  if (req.query.name === undefined) {
    res.json({
      error: "Please provide a name!"
    })
  } else if (req.query.title === undefined) {
    res.json({
      error: "Please provide a title!"
    })
  } else {
    res.json({
      welcome_message: `Oh, hi there ${name}, my dear ${title}!`
    })
  }
})

app.get('/appenda/:appendable', (req, res) => {
  const appendable = req.params.appendable;
  if (appendable !== undefined) {
    res.json({
      appended: `${appendable}a`
    })
  } else {
    res.status(404)
  }
})

app.push('/dountil/:what', (req, res) => {
  const number = req.body.until;
  const operation = req.params.what;
  if (operation === 'sum') {
    res.json({
      result: 
    })
  }


})

app.listen(8080);