#!/usr/bin/node

require('process');
const myArgv = process.argv;
const size = myArgv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
