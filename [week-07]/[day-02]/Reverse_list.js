'use strict';

let matrix = [];

function create_matrix(size) {
  
  for (var j = 0; j < size; j++) {
    matrix.splice(j, 0, [])
    for (var i = 0; i < size; i++) {
      matrix[j].splice(2, 0, 0);
    }
  }
  var counter = size-1;
  for (var k = 0; k < size; k++) {
    matrix[k][counter] = 1;
    counter -= 1;
  }

}

create_matrix(4);
console.log(matrix);