#!/usr/bin/node
'use strict';

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    const ch = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(ch.repeat(this.width));
    }
  }
}

module.exports = Square;
