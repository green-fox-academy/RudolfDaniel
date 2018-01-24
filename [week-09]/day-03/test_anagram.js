'use strict';

let test = require('tape');
let anagramma = require('./anagram.js');

test('is_anagram', function (t) {
  var actual = anagramma('ez egy anagramma', 'maga nemez ragya');
  var expected = true;

  t.equal(actual, expected);
  t.end();
});

test('is_anagram', function (t) {
  var actual = anagramma('ez egy anagramma', 'ez nem egy anagramma');
  var expected = false;

  t.equal(actual, expected);
  t.end();
});