const url = 'https://swapi.co/api/films/?format=json';

$.ajax({url})
.done((req) => {
    for (let i in req.results) {
        $('#list_movies').append('<li>' + req.results[i].title + '</li>');
    }
})