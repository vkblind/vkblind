require([
    'jquery'
],

function ($) {

    html = $("html");
    a = $("a");

    $(document).ready(function(){
        if (localStorage.getItem("is_inverted") == "true"){
            html.addClass("inverted");
            a.addClass("inverted");
        } else {
            html.removeClass("inverted");
            a.removeClass("inverted");
        }
    });

    $("#invert").click(function(){
        if (html.hasClass("inverted") && a.hasClass("inverted")) {
            html.removeClass("inverted");
            a.removeClass("inverted");
            localStorage.setItem("is_inverted", false);
        } else {
            html.addClass("inverted");
            a.addClass("inverted");
            localStorage.setItem("is_inverted", true);
        }
    });
});
