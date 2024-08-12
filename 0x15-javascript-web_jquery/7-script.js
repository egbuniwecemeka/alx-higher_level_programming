// Fetches the character name from a URL

$(document).ready(function () {
    //GET
    $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
        $("#character").text(data.name)
    });
});
