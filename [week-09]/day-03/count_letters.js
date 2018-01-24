'use strict';

let countLetters = function (string) {
  var stringObject = {};
  for (var i = 0; i < string.length; i++) {
    if (stringObject[string[i]] === undefined) {
      stringObject[string[i]] = 1;
    } else {
      stringObject[string[i]] += 1;
    }
  }
  return stringObject;
}
console.log(countLetters('ez egy anagramma'));

module.exports = countLetters;