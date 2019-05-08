#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else if (n > 0) {
  for (let v of Array(n).fill('C is fun')) {
    console.log(v);
  }
}
