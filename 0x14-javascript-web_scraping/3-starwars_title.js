#!/usr/bin/node
require('request').get(`http://swapi.co/api/films/${process.argv[2]}`,
  (err, resp) => console.log(err || JSON.parse(resp.body).title));
