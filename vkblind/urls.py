# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import groups.urls
import ims.urls
import feed.urls
from views import login, logout, index, profile, settings, save_settings, search


urlpatterns = patterns('',
    url(r'^$', include(groups.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', search, name='search'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^im/', include(ims.urls)),
    url(r'^feed/', include(feed.urls)),
    url(r'^groups/', include(groups.urls)),
    url(r'^accounts/login/$', login),
    url(r'^profile/(?P<vkuser>.+)$', profile, name='profile'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/save/$', save_settings, name='save_settings'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += staticfiles_urlpatterns()
