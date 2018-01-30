'use strict';

const express = require('express');

const app = express();

app.use('/', express.static('Public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/Foxplayer.html');
});

const playlists = [
  { 'id': 0, 'title': 'All tracks', 'system': 1},
  { 'id': 1, 'title': 'Favorites', 'system': 1},
  { 'id': 2, 'title': 'Test', 'system': 0},
  { 'id': 3, 'title': 'Test', 'system': 0},
  { 'id': 4, 'title': 'Test', 'system': 0},
]

app.get('/playlists', (req, res) => {
  res.json(playlists)
});

app.listen(8000);