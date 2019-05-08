#!/usr/bin/node
const n = parseInt(process.argv[2]);
console.log(isNaN(n) ? 'Not a number' : `My number: ${n}`);
