function Animal() {
  this.hunger = 5,
  this.thirst = 5,
  this.eat = function() {
    this.hunger --
  }
  this.drink = function() {
    this.thirst --
  }
  this.play = function() {
    this.thirst ++
    this.hunger ++
  }
}

function Farm(place) {
  this.place = place
  this.animals = []
  this.breed = function() {
    if (this.animals.length < this.place) {
      this.animals.push(new Animal())
    }
  }
  this.slaughter = function() {
    var min_hunger = animals[0].hunger;
    var min_index = 0;
    for (var i = 0; i < this.animals.length; i++) {
      if (animals[i].hunger < min_hunger) {
        min_hunger = animals[i].hunger;
        min_index = i;
      }
    }
  }
}


// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

SheepFarm.breed();

console.log(SheepFarm.animals.length);
console.log(SheepFarm.animals[0].hunger); // Should log 20 Animal objects
/*
const button = document.querySelector('button');
*/
// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full