'use strict';

/*
  Remove the king from the list.
  Fill the list based on the following list of objects.
  Only add the asteroids to the list.
  Each list item should have its category as a class and its content as text content. -->
*/


let ruler = document.querySelector('ul');
let king = document.querySelector('li');
ruler.removeChild(king);
console.log(ruler);


const planetData = [
  {
    category: 'inhabited',
    content: 'Foxes',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Whales and Rabbits',
    asteroid: true
  },
  {
    category: 'uninhabited',
    content: 'Baobabs and Roses',
    asteroid: true
  },
  {
    category: 'inhabited',
    content: 'Giant monsters',
    asteroid: false
  },
  {
    category: 'inhabited',
    content: 'Sheep',
    asteroid: true
  }
]


for (var i = 1; i < planetData.length; i++) {
  if (planetData[i].asteroid = true) {
    let newPlanet = document.createElement('li');
    ruler.appendChild(newPlanet);
    newPlanet.textContent = planetData[i].content;
    newPlanet.classList.add(planetData[i].category);
  }
}