'use strict';

let elements = document.getElementsByTagName('li');
elements[0].innerText = 'apple';
elements[1].innerText = 'banana';
elements[2].innerText = 'cat';
elements[3].innerText = 'dog';

for (var i = 0; i < elements.length; i++) {
  elements[i].style.backgroundColor = 'limegreen';
}