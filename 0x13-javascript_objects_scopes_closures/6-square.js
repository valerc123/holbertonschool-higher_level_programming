#!/usr/bin/node

const square = require('./5-square');


class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      console.log("X")
      for (let i = 0; i < this.size; i++) {
        console.log("C".repeat(this.size))
      }


  }

}

module.exports = Square;
