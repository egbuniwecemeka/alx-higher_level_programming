// JQuery toggling css class of an HTML element

/* global $ */

$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green').addClass('red');
    } else {
      $('header').removeClass('red').addClass('green');
    }
  });
});
