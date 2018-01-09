'use strict';

function sum(number) {
  sum = 0;
  for (var i = 0; i < number+1; i++) {
    sum += i;
  }
  return sum;
}

console.log(sum(5));