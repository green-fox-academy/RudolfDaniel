'use strict';

var lineCount = 6;

console.log('%'.repeat(lineCount));

for (var i = 0; i <= lineCount-3; i++) {
    console.log('%' + ' '.repeat(i) + '%' + ' '.repeat(lineCount-3-i) + '%');
}

console.log('%'.repeat(lineCount));