'use strict';

let test = require('tape');
let fibonacci = require('./fibonacci.js');

test('counter', function (t) {
  var actual = fibonacci(6);
  var expected = 8;

  t.equal(actual, expected);
  t.end();
});