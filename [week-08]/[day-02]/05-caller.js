'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(array, callback) {
  var last_even = array[0];
  var evens = array.filter(function(e) {
    if (e % 2 === 0) {
      last_even = e;
    };
  });
  callback(last_even)
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8