# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from views import view_groups, view_group, search_groups


urlpatterns = patterns('',
    url(r'^$', view_groups, name='view_groups'),
    url(r'^(\d+)/$', view_group, name='view_group'),
    url(r'^search-groups/$', search_groups, name='search_groups'),
)
