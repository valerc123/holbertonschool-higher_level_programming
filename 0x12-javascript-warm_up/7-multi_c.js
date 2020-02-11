#!/usr/bin/node

require('process');

const myArgv = process.argv;

if (isNaN(myArgv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(myArgv[2]); i++) {
    console.log('C is fun');
  }
}
