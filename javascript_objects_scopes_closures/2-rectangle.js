#!/usr/bin/node
'use strict';

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
