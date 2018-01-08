'use strict';

var lineCount = 7;

for (var i = 0; i <= lineCount; i++) {
    console.log(' '.repeat(lineCount - i) + '*'.repeat(2*i));
}

for (var i = lineCount; i > 0; i = i - 1) {
    console.log(' '.repeat(lineCount - i) + '*'.repeat(2*i-1));
}