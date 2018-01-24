'use strict';

const addNumbers = function(a, b) {
  if (typeof b !== 'number') {
    throw new Error('Invalid value');
  }
  return a + b;
}

const maxOfThree = function(a, b, c) {
  if (typeof a !== 'number') {
    throw new Error('Invalid value');
  } else if (typeof b !== 'number') {
    throw new Error('Invalid value');
  } else if (typeof c !== 'number') {
    throw new Error('Invalid value');
  }
  if (a > b) {
    return a;
  } else {
    return c;
  }
}

//Returns the median value of a list given as param
const median = function(pool){
  return(pool[(pool.length - 1) / 2]);
}

// Returns true if the param is a vovel
const isVovel = function(char){
  var index = 'aeiouéáőűöüóí'.indexOf(char);
  if (index === -1) {
    return false;
  } else {
    return true;
  }
}

// Create a method that translates hungarian into the teve language
const translate = function(hungarian) {
  let text = hungarian.split('');
  let teve = '';
  text.forEach(function(char){
    if (isVovel(char)){
      teve += char + 'v'+ char;
    }
  });
  return teve;
}

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}