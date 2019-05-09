#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing size');
} else if (times > 0) {
  for (const ch of 'X'.repeat(times)) {
    console.log(ch.repeat(times));
  }
}
