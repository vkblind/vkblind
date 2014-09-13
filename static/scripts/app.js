define([
    'underscore',
    'backbone',
    'marionette',

    'modules/header',
    'modules/news'
],

function (_, Backbone, Marionette, header, news) {
    var app = new Backbone.Marionette.Application();

    app.addRegions({
        headerRegion: '#js-app-header',
        mainRegion: '#js-app-content'
    });

    app.addInitializer(function () {
        this.root = '/';
    });

    app.module('header', header);
    app.module('news', news);

    return app;
});
