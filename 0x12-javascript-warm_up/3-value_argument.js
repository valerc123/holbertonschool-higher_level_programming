#!/usr/bin/node

require('process');

const myArgv = process.argv;

if (!myArgv[2]) {
  console.log('No argument');
} else {
  console.log(myArgv[2]);
}
