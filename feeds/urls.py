# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from views import view_feeds


urlpatterns = patterns('',
    url(r'^$', view_feeds),
)
