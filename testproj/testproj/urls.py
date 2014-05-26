#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'testproj.views',
    url(r'^$', 'index', name='home'),
    url(r'^basic/$', 'basic', name='basic'),
    url(r'^preview/$', 'preview', name='preview'),
    url(r'^post/list/$', 'post_list', name='post_list'),
    url(r'^post/add/$', 'post_create', name='post_create'),
    url(r'^post/(?P<pk>\d+)/$', 'post_update', name='post_update'),
)
