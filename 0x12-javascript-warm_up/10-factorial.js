#!/usr/bin/node

require('process');
const myArgv = process.argv;
const num = parseInt(myArgv[2]);

function factorial (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
