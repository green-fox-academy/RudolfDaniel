'use strict';

let asteroids = document.querySelector('ul.asteroids');

let newAsteroid = document.createElement('li');
asteroids.appendChild(newAsteroid);
newAsteroid.textContent = 'The Green Fox';

let lampLighter = document.createElement('li');
asteroids.appendChild(lampLighter);
lampLighter.textContent = 'The Lamplighter';

let container = document.querySelector('.container');
let heading = document.createElement('h1');
container.appendChild(heading);
heading.textContent = 'I can add elements to the DOM!';

let image = document.createElement('img');
container.appendChild(image);
image.src = 'no-image.png';