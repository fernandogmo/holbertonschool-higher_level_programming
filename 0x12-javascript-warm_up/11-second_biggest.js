#!/usr/bin/node
console.log(process.argv[3]
  ? process.argv.slice(2)
    .map(Number)
    .sort((a, b) => a - b)
    .slice(-2)[0] : 0);
