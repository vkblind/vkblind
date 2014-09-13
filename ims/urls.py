# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from views import view_messages


urlpatterns = patterns('',
    url(r'^$', view_messages),
)
