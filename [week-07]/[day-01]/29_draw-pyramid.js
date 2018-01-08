'use strict';

var lineCount = 4;

for (var i = 1; i <= lineCount; i++) {
    console.log(' '.repeat(lineCount - i) + '*'.repeat(2*i-1));
}