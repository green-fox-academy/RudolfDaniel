'use strict';

let tanks = [
  {
    image_url: 'kv-2.jpg',
    content: 'KV-2'
  },
  {
    image_url: 'maus.png',
    content: 'Maus'
  },
  {
    image_url: 'sherman.jpg',
    content: 'Sherman'
  },
  {
    image_url: 'sturmtiger.jpg',
    content: 'Sturmtiger'
  },
  {
    image_url: 't-28.jpg',
    content: 'T-28'
  },
  {
    image_url: 't-34.jpg',
    content: 'T-34'
  },
  {
    image_url: 'tiger.jpg',
    content: 'Tiger'
  },
  {
    image_url: 'zrinyi_II.jpg',
    content: 'Zrínyi II'
  },
]

let images = document.querySelector('.thumbnail');
let text = document.querySelector('.label');
text.innerText = tanks[0].content;

function letimage(a) {
  let element = document.createElement('li');
  element.innerHTML = "<button><img src='" + tanks[a].image_url + "' width='39' height='39'></button>"
  images.appendChild(element);
}

for (var i = 0; i < tanks.length; i++) {
  letimage(i);
}

let first_image = document.querySelectorAll('li button img')[0];
let display = document.getElementsByClassName('main_image');

let source = first_image.src;

display[0].style.backgroundImage = 'url(' + source + ')';

