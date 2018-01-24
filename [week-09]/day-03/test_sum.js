'use strict';

let test = require('tape');
let summarum = require('./sum.js');

test('sum', function (s) {
  var actual = summarum.getSum([1, 2, 3]);
  var expected = 6;

  s.equal(actual, expected);
  s.end();
});

test('sum', function (s) {
  var actual = summarum.getSum([]);
  var expected = 0;

  s.equal(actual, expected);
  s.end();
});

test('except when not array', function (t) {
  t.throws(summarum.getSum.bind(null, null), TypeError)
  t.end();
}
)