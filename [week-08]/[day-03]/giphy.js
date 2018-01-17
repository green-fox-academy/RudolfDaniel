'use strict';
/*
let gifs = []
*/

let firstgif = new XMLHttpRequest();


firstgif.open("GET", "http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=jrr0XR1sMJCpdtiGSgc5FW7n6sAFzphS&limit=1");
firstgif.send( null );

firstgif.onreadystatechange = function() {
  if (firstgif.readyState === 4 && firstgif.status === 200) {
    let url = JSON.parse(firstgif.response);
    console.log(url);
    letimage(url.data[0].images.original.url);
  }
};



let image = document.querySelector('.main_image');



function letimage(source_url) {
  let element = document.createElement('div');
  element.innerHTML = "<img src='" + source_url + "' width='39' height='39'>"
  image.appendChild(element);
}

/*
for (var i = 0; i < tanks.length; i++) {
  letimage(i);
}

let first_image = document.querySelectorAll('li button img')[0];
let display = document.getElementsByClassName('main_image');

let source = first_image.src;

display[0].style.backgroundImage = 'url(' + source + ')';
*/