#!/usr/bin/node
require('request').get(process.argv[2],
  (err, resp) => console.log(err || countFilms('18', JSON.parse(resp.body).results)));

function countFilms (id, films) {
  return films.filter((film) => film.characters.find((character) => character.includes(id))).length;
}
