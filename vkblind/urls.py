# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = patterns('',
    url(r'^$', include('groups.urls')),

    url(r'^logout/$', views.logout, name='logout'),
    url(r'^accounts/login/$', views.login),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^im/', include('ims.urls')),
    url(r'^feed/', include('feed.urls')),

    url(r'^groups/', include('groups.urls')),
    url(r'^club/', include('groups.urls')),  # TODO нужно пока не сделаем урлы вида vkblind.com/monitoringe

    url(r'^settings/', include('vkblind.user_settings.urls')),
    url('', include('search.urls')),

    url(r'^help/$', views.help_page, name='help_page'),

    url(r'^profile/(?P<vkuser>.+)$', views.profile, name='profile'),
    url(r'^id/(?P<vkuser>.+)$', views.profile),   # TODO нужно пока не сделаем урлы вида vkblind.com/monitoringe

    url('', include('social.apps.django_app.urls', namespace='social')),
)

urlpatterns += staticfiles_urlpatterns()
