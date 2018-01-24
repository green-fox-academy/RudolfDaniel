'use strict';

let sum = {
  getSum: function(numbers) {
    if (!Array.isArray(numbers)) {
      throw new TypeError('input is not an array!!!!!!!!!!!');
    }
    var summa = numbers.reduce(add, 0);
    function add(a, b) {
      return a + b;
    }
    return summa;
  }
}

console.log(sum.getSum([1,2,3]));

module.exports = sum;