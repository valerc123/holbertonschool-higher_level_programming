#!/usr/bin/node

require('process');

const myArgv = process.argv;

const a = parseInt(myArgv[2]);
const b = parseInt(myArgv[3]);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
add(a, b);
