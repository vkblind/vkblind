# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.settings, name='settings'),
    url(r'^save$', views.save_settings, name='save_settings'),
)
