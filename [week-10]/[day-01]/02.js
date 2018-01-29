'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

class Rectangle {
  constructor(a, b) {
    this.aSide = a;
    this.bSide = b;
  }

  getArea(aSide, bSide) {
    return this.aSide * this.bSide;
  }

  getCircumference(aSide, bSide) {
    return this.aSide * 2 + this.bSide * 2;
  }

}

const brick = new Rectangle(10, 20);

console.log(brick.getArea());
console.log(brick.getCircumference());
