const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.ajax({ url: url })
  .done((req) => {
    $('#hello').append('<li>' + req.hello + '</li>');
  });
