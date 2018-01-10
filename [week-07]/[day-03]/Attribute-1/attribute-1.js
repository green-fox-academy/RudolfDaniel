'use strict';

let image_url = document.querySelector('img');
console.log(image_url.getAttribute('src'));

image_url.src = '1200px-Okapi2.jpg';

let link_of_webpage = document.querySelector('a');
link_of_webpage.href = 'https://www.greenfoxacademy.com/';

let second_button = document.querySelector('button');
second_button.disabled = true;
second_button.textContent = 'Don\'t click me!';