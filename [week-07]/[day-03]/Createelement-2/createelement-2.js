'use strict';

let candies = document.querySelector('ul');
let candy_1 = document.querySelector('li');
candies.removeChild(candy_1);
console.log(candies);

for (var i = 1; i < 17; i++) {
  let newCandy = document.createElement('li');
  candies.appendChild(newCandy);
  newCandy.textContent = 'Empty box #' + i;
}