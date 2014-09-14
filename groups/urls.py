# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from views import view_groups


urlpatterns = patterns('',
    url(r'^$', view_groups, name='view_groups'),
)
