'use strict';

let audio = document.querySelector('audio');
audio.onloadstart = function() {
  console.log('Starting to load audio');
}

let media = document.querySelector('audio');

let button = document.querySelector('button');

button.addEventListener('click', function(e) {
  if (media.paused) {
    media.play();
    console.log('clicked to play');
  } else {
    media.pause();
    console.log('clicked to pause');
  }
}, false);

