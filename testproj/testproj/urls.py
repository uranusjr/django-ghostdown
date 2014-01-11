#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'testproj.views.index'),
)
