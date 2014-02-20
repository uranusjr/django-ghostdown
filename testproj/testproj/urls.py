#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'testproj.views.index'),
    url(r'^basic/$', 'testproj.views.basic', name='basic'),
    url(r'^preview/$', 'testproj.views.preview', name='preview'),
)
