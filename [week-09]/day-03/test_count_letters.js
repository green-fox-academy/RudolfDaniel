'use strict';

let test = require('tape');
let countLetters = require('./count_letters.js');

test('counter', function (t) {
  var actual = countLetters('letter');
  var expected = { 'l': 1, 'e': 2, 't': 2, 'r': 1 };

  t.deepEqual(actual, expected);
  t.end();
});