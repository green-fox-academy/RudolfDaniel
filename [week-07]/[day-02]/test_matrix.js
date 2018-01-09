let size = 4;
let myMatrix = [];

for (let i = 0; i < size; i++) {
  myMatrix.push('0 '.repeat(size - 1) + '1 ' + '0 '.repeat(i));
}

console.log(myMatrix);