$('#toggle_header').click(() => {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else if ($('header').hasClass('green')) {
    $('header').toggleClass('red');
  }
});
