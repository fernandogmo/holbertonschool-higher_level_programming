#!/usr/bin/node
require('fs').writeFile(process.argv[2], process.argv[3], 'utf-8',
  (err) => { if (err) console.log(err); });
