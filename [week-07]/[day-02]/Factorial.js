'use strict';

function factorio(number) {
  factorio = 1;
  for (var i = 1; i < number+1; i++) {
    factorio = i * factorio;
  }
  return factorio;
}

console.log(factorio(4));