'use strict';

const express = require('express');
const mysql = require('mysql');

const app = express();

app.use('/', express.static('public'));
app.use(express.json());

const conn = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'vizsga',
});

conn.connect(function(err){
  if(err){
    console.log("Error connecting to Db");
    return;
  }
  console.log("Connection established");
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

let testProduct = {
  'id': '1',
  'item_name': 'Strecth Steamed Pencil Skirt',
  'manufacturer': 'Calvin Klein',
  'category': 'skirts',
  'size': 's',
  'unit_price': 39.0,
  'in_store': 10,
};

app.get('/warehouse', (req, res) => {
  conn.query('SELECT * FROM warehouse;', (err, rows) => {
    if(err) {
      console.log(err.toString());
      res.status(500).send('Database error');
      return;
    }
  //testProduct.push({})
  //console.log(rows);
  res.json(rows);
  //res.json(testProduct);
  })
});

app.get('/price-check', (req, res) => {
  conn.query(`SELECT in_store FROM warehouse WHERE item_name = "${req.query.item}"`, (err, rows) => {
    console.log(req.query.item);
    console.log(rows);
  })
  /*
  if (req.query.quantity <= testProduct.in_store && req.query.item === testProduct.item_name) {
    res.json({ price: `<h5 style="background-color:green;">The items can be ordered at the ${testProduct.unit_price} price.` });
  } else {
    res.json({ price: `<h5 style="background-color:red;">error, we don't have enough items in store</h5>` });
  }
  */
});

app.listen(8000);