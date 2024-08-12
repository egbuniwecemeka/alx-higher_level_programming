// JQuery that updates the content of tag element on clicking an event

$(document).ready(function () {
    $("#update_header").click(function () {
        $("header").text("New Header!!!")
    })
});