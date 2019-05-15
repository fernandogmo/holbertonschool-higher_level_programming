#!/usr/bin/node
require('request').get('http://swapi.co/api/people/18',
  (err, resp) => console.log(err || JSON.parse(resp.body).films.length));
