'use strict';

var a = 24;
var out = 0;

if (a % 2 === 0) {
    out ++;
}

console.log(out);


var b = 13;
var out2 = '';

if (b > 10 && b < 20) {
    out2 = 'less';
} else if (b > 20) {
    out2 = 'more'
}

console.log(out2);


var c = 123;
var credits = 100;
var isBonus = false;

if (credits >= 50 && isBonus != true) {
    c -= 2;
} else if (credits < 50 && isBonus != true) {
    c -= 1;
}

console.log(c)


var d = 8;
var time = 120;
var out3 = '';

if (d % 4 === 0 && time <= 200) {
    out3 = 'check';
} else if (time > 200) {
    out3 = 'Time out';
} else {
    out3 = 'Run Forest Run!';
}

console.log(out3);