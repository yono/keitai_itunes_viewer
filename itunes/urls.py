# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('keitai.itunes.views',
    (r'^$', 'index'),
    (r'^(?P<artist_id>\d+)/(?P<album_id>\d+)/$', 'album'),
    (r'^(?P<artist_id>\d+)/$', 'artist'),
)
