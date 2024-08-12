// A JS script that updates header tag text color to red on clicking an event

$(document).ready(function () {
    $("#red_header").click(function () {
        $("header").css("color", "#FF0000");
    });
});