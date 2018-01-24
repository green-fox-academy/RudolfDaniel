'use strict';

let anagram = function (firstText, secondText) {
  var firstString = firstText.split('').sort();
  var secondString = secondText.split('').sort();
  for (var i = 0; i < firstString.length; i++) {
    if (firstString.length === secondString.length) {
      if (firstString[i] === secondString[i]) {
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  }
}
console.log(anagram('ez egy anagramma', 'maga nemez ragya'));

module.exports = anagram;