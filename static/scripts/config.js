requirejs.config({
    deps: ['main'],
    paths: {
        tpl: '../bower_components/requirejs-tpl/tpl',
        backbone: '../bower_components/backbone/backbone',
        jquery: '../bower_components/jquery/dist/jquery',
        marionette: '../bower_components/marionette/lib/backbone.marionette',
        underscore: '../bower_components/underscore/underscore',
        templates: 'templates'
    },
    shim: {
        backbone: {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        underscore: {
            exports: '_'
        }
    }
});
