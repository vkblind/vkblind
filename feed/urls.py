# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from views import view_feed


urlpatterns = patterns('',
    url(r'^$', view_feed, name='view_feed'),
)
