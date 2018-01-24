'use strict';

let fibonacci = function (index) {
  if (index < 2) {
    return index;
  } else {
    return ((fibonacci(index-1) + (fibonacci(index-2))));
  }
};

console.log(fibonacci(6));

module.exports = fibonacci;