define([
    'backbone',
    'marionette',
    'tpl!templates/header.html'
], function (Backbone, Marionette, headerTemplate) {
    var HeaderView = Marionette.ItemView.extend({
        className: 'container',

        template: headerTemplate,

        ui: {
            sections: '[data-section]'
        },

        modelEvents: {
            'change': 'render'
        },

        highlight: function (section) {
            this.currentSection = section;
            this.ui.sections
                .filter('[data-section="' + section + '"]').addClass('active')
                .siblings().removeClass('active');
        },

        onRender: function () {
            this.highlight(this.currentSection);
        }
    });

    return function (module, app) {
        var headerView = new HeaderView({
            model: new Backbone.Model()
        });

        app.headerRegion.show(headerView);
        app.mainRegion.on('show', function (view) {
            var section = view.sectionName || '';
            app.headerRegion.currentView.highlight(section);
        });

        app.on('start', function (options) {
            headerView.model.set(options.currentUser);
        });
    };
});
