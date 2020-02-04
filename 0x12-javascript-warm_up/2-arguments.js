#!/usr/bin/node

require('process');

const myArgv = process.argv;

if (myArgv.length === 2) {
  console.log('No argument');
} else if (myArgv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
