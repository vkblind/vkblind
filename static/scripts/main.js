require([
    'jquery'
],

function ($) {

    html = $("html");

    $(document).ready(function(){
        if (localStorage.getItem("is_inverted") == "true"){
            html.addClass("inverted");
        } else {
            html.removeClass("inverted");
        }
    });

    $("#invert").click(function(){
        if (html.hasClass("inverted")) {
            html.removeClass("inverted");
            localStorage.setItem("is_inverted", false);
        } else {
            html.addClass("inverted");
            localStorage.setItem("is_inverted", true);
        }
    });
});
