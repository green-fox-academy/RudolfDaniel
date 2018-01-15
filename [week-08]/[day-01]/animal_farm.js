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

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
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
    this.animals.pop(animals[min_index]);
  }
  this.progress = function() {
    for (var i = 0; i < this.animals.length; i++) {
      if (getRandomInt(2) === 0) {
        this.animals[i].eat()
      }
      if (getRandomInt(2) === 0) {
        this.animals[i].drink()
      }
      if (getRandomInt(2) === 0) {
        this.animals[i].play()
      }
    }
  if (this.animals.length === 0) {
    console.log('bankrupt')
  } else if (this.animals.length > 0 && this.animals.length < this.place) {
    console.log('okay')
  } else if (this.animals.length === this.place) {
    console.log('full')
  }
  console.log('Number of animals ' + this.animals.length)
  }
}

// Create a sheep farm with 20 slots
const SheepFarm = new Farm(20);

SheepFarm.breed();

console.log(SheepFarm.animals.length);
console.log(SheepFarm.animals[0].hunger);

SheepFarm.progress();

// Should log 20 Animal objects

const button = document.querySelector('button');

button.addEventListener('click', SheepFarm.progress.bind(SheepFarm));

// Add a click event to the button and call 'progress'

// The progress function should log the following to the console:
//  - The farm has 20 living animals, we are full