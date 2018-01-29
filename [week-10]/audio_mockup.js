'use strict';

let audio = document.querySelector("audio");
audio.onloadstart = function() {
  console.log("Starting to load audio");
}