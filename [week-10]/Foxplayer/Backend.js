'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use('/', express.static('Public'));
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/Foxplayer.html');
});

const playlists = [
  { 'id': 0, 'title': 'All tracks', 'system': 1},
  { 'id': 1, 'title': 'Favorites', 'system': 1},
  { 'id': 2, 'title': 'Test', 'system': 0},
]

app.get('/playlists', (req, res) => {
  res.json(playlists)
});

app.post('/playlists', (req, res) => {
  let newPlayList = { 'id': playlists.length, 'title': req.body.title, 'system': 0 };
  playlists.push(newPlayList);
  res.json(newPlayList);
});

app.listen(8000);