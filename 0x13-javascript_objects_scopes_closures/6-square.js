#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      console.log(Array(this.height).fill(c.repeat(this.width)).join('\n'));
    }
  }
};
