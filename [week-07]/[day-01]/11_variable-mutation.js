'use strict';

var a = 3;

console.log(a);

a += 7;

console.log(a);



var b = 100;

console.log(b);

b -= 7;

console.log(b);


var c = 44;

console.log(c);

c *= 2;

console.log(c);


var d = 125;

console.log(d);

d /= 5;

console.log(d);


var e = 8;

console.log(e);

var e = e ** 2;

console.log(e);


var f1 = 123;
var f2 = 345;

if (f1 > f2) {
    console.log(true);
}


var g1 = 350;
var g2 = 200;

if ((g2 * 2) > g1) {
    console.log(true);
}


var h = 1357988018575474;

if (h % 11 === 0) {
    console.log(true);
}


var i1 = 10;
var i2 = 3;

if (i1 > i2*i2*i2 && i1 < i2*i2) {
    console.log(true);
} else {
    console.log(false);
}


var j = 1521;

if (j%3 === 0 && j%5 === 0) {
    console.log(true);
} else {
    console.log(false);
}


var k = 'Apple';

console.log(k + k + k + k);