// A JSQuery that adds a class to an HTML element on a click event

/* global $ */
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
