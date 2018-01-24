'use strict';

let test = require('tape');
let countLetters = require('./count_letters.js');

test('is_anagram', function (t) {
  var actual = anagramma('ez egy anagramma');
  var expected = true;

  t.equal(actual, expected);
  t.end();
});