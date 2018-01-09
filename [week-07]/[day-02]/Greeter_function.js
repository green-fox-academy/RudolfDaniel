'use strict';

let al = 'Greenfox';

function greet(name) {
  if (name === undefined) {
    console.log('Noone to greet. :(')
  } else {
    console.log('Greetings, dear ' + name);
  }
}

greet(al);