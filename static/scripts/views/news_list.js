define([
    'jquery',
    'marionette',
    'tpl!templates/news_list.html'
], function ($, Marionette, newsListTemplate) {
    return function (module, app) {
        var NewsListView = Marionette.CollectionView.extend({
            template: newsListTemplate
        });
    };
});
