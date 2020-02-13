const url = 'https://swapi.co/api/people/5/?format=json';

$.ajax({url: url})
.done((req) => {
    $('#character').text(req.name);
});