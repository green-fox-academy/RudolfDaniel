'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/', express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/Index.html');
});

app.get('/search', (req, res) => {
  res.json({
    message: "This is your licence plates"
  })
});

app.post('/playlists', (req, res) => {
  console.log("Data sent");
  /*
  let newPlayList = { 'id': playlists.length, 'title': req.body.title, 'system': 0 };
  playlists.push(newPlayList);
  res.json(newPlayList);
  */
});

app.listen(8000);