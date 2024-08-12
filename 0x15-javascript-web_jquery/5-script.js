// Adds a <li> element to a list when user clicks DIV#add_item tag

/* global $ */
$(document).ready(function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
});
