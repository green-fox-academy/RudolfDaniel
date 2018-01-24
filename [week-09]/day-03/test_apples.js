'use strict';

let test = require('tape');
let apple = require('./apples.js');

test('get apple', function (a) {
  var actual = apple.getApple();
  var expected = 'apple';

  a.equal(actual, expected);
  a.end()
});