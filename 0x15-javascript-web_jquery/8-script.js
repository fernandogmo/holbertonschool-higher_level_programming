$.get('https://swapi.co/api/films/?format=json', (data) =>
  data.results.forEach((film) =>
    $('ul#list_movies').append(`<li>${film}</li>`)));
