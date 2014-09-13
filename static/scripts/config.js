requirejs.config({
    deps: ['main'],
    paths: {
        backbone: '../bower_components/backbone/backbone',
        jquery: '../bower_components/jquery/jquery',
        marionette: '../bower_components/marionette/lib/core/amd/backbone.marionette',
        underscore: '../bower_components/underscore/underscore',
        templates: 'templates/compiled'
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
