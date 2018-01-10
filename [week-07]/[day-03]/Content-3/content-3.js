'use strict';

let first_line = document.getElementsByTagName('p')[0];

let second_line = document.getElementsByClassName('output1')[0];
second_line.innerText = first_line.textContent;

let third_line = document.getElementsByClassName('output2')[0];
third_line.innerHTML = first_line.innerHTML;