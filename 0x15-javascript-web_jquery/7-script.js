$.get('https://swapi.co/api/people/5/?format=json', (data) => $('div#character').html(data.name));
