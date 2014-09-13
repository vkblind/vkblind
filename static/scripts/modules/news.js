define([
    'jquery',
    'backbone',
    'data/news',
    'views/news_list'
], function ($, Backbone, News, NewsListView) {
    return function (module, app) {

        var Router = Backbone.Router.extend({
            routes: {
                '': 'newsList'
            },

            newsList: function () {
                app.mainRegion.show(new NewsListView({
                    collection: module.collection
                }));
            }
        });

        module.collection = new News();
        module.router = new Router();

        app.on('start', function () {

        });
    };
});
