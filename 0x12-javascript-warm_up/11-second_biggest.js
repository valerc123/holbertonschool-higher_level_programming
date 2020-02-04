#!/usr/bin/node

process.argv.splice(0, 2);
const max = Math.max(...process.argv);
const newArray = process.argv.filter(ele => ele !== max.toString());
console.log(Math.max(...newArray));
