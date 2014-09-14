# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import groups.urls
import ims.urls
import feed.urls
from views import login, logout, index, profile


urlpatterns = patterns('',
    url(r'^$', index, name='home'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^logout/$', logout, name='logout'),
    url(r'^im/', include(ims.urls)),
    url(r'^feed/', include(feed.urls)),
    url(r'^groups/', include(groups.urls)),
    url(r'^accounts/login/$', login),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^(?P<vkuser>.+)$', profile)
)

urlpatterns += staticfiles_urlpatterns()
