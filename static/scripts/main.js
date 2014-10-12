require([
    'jquery',
    'underscore',
    'backbone',
    'marionette',
],

function ($, _, BB, TT) {
    window.searcher = {
        views: {}
    };

    // searcher.views.search = BB.View.extend({});
    // searcher.views.groups = BB.View.extend({});
    // searcher.views.users = BB.View.extend({});
    // searcher.model = BB.Model.extend({});

    Rotate = BB.View.extend({
        events: {
            'click .next': 'toNext',
            'click .prev': 'toPrev',
        },

        initialize: function (model, url, container, template) {
            this.model = model;
            this.url = url;
            this.container = container;
            this.template = this.getTemplate();
        },

        getTemplate: function () {
            return "<div>Hello world!</div>";
        },

        toNext: function () {
            var self = this;
            $.get({
                url: self.url,
                success: function(result) {
                    self.render(result);
                }
            });
        },

        toPrev: function () {

        },

        render: function (context) {
            var self = this;
            var result = _.template(self.template, context);
            self.container.html(result);
        }
    });

    Model = BB.Model.extend({
        defaults: {
            query: null,
            count: 20,
            users_offset: 0,
            groups_offset: 0
        }
    });
    model = new Model();


    Router = BB.View.extend({
        events: {
            'asdf': 'home'
        },
        home: function() {
            alert('hello');
        }
    });
    searcher.router = new Router();
    // BB.history.start({pushState: true, root: '/'});
    searcher.router.trigger('asdf');
});
