'use strict';

var ai = [3, 4, 5, 6, 7];

var sum_of_ai = ai.reduce(add, 0);

function add(a, b) {
  return a + b;
}

console.log(sum_of_ai);