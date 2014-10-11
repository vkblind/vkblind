# -*- coding: utf-8 -*-

__author__ = "chipiga86@yandex.ru"

from django.conf.urls import patterns, url

from views import search


urlpatterns = patterns('',
    url(r'^search/$', search, name='search')
)