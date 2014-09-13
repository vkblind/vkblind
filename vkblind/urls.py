# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

import ims.urls
import feeds.urls
from views import login, logout


urlpatterns = patterns('',
    url(r'^$', 'vkblind.views.index', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^im/', include(ims.urls)),
    url(r'^feed/', include(feeds.urls)),
)
