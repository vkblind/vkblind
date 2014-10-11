require([
    'jquery'
],

function ($) {
    $(document).ready(function () {
        $('input').addClass($('html').attr('class'));
    });
});
