#!/usr/bin/node
require('request').get(process.argv[2],
  (err, resp) => console.log(err || `code: ${resp.statusCode}`));
