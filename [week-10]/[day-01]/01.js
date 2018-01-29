'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(sound) {
  let talk = sound;

  function say() {
    console.log(talk);
  }

  return {
    talk: talk,
    say: say,
  }
}

let dog = Animal('wau');
dog.say();