'use strict';

let aj = [3, 4, 5, 6, 7];

aj.reverse();

console.log(aj);

let new_aj = [];

for (var i = aj.length; i > -1; i -= 1) {
  new_aj.push(aj[i]);
}

console.log(new_aj);