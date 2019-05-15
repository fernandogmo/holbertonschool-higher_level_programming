#!/usr/bin/node
require('fs').readFile(process.argv[2], 'utf-8',
  (err, data) => console.log(err || data));
