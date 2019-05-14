#!/usr/bin/node
exports.converter = function (base) {
  return val => val.toString(base);
};
