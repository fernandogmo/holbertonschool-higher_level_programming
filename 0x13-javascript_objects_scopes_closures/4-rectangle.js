#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (const ch of 'X'.repeat(this.height)) {
      console.log(ch.repeat(this.width));
    }
  }
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
