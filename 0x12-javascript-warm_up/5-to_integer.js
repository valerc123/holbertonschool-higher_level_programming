#!/usr/bin/node

require('process');
const myArgv = process.argv;

if (isNaN(myArgv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myArgv[2]));
}
