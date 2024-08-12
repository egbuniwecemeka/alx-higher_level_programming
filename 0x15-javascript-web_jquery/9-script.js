// JS script that fetches a response from a URL, and displays it on a tag

$(document).ready(function () {
    // Cache DOM selector
    const $greeting = $("#hello");

    $.ajax({
        type: 'GET',
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        success: function (greets) {
            $greeting.text(greets.hello);
        }
    });
});