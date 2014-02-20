#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from appconf import AppConf


__all__ = ['GhostdownConf', 'settings']


DEFAULTS = {   # Default setting values
    'JQUERY_URL': '//code.jquery.com/jquery-1.10.1.min.js',
    'CODEMIRROR_JS_URL': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/3.20.0/codemirror.min.js'
    ),
    'CODEMIRROR_MARKDOWN_JS_URL': (
        '//cdnjs.cloudflare.com/ajax/libs/codemirror/3.20.0/mode/markdown/'
        'markdown.min.js'
    ),
    'SHOWDOWN_JS_URL': (
        '//cdnjs.cloudflare.com/ajax/libs/showdown/0.3.1/showdown.min.js'
    )
}


def _get_setting(key, fallback_key=None):
    if fallback_key is None:
        fallback_key = key
    return getattr(settings, key, DEFAULTS[fallback_key])


# Load Appconf
class GhostdownConf(AppConf):
    JQUERY_URL = _get_setting('JQUERY_URL')
    CODEMIRROR_JS_URL = _get_setting('CODEMIRROR_JS_URL')
    CODEMIRROR_MARKDOWN_JS_URL = _get_setting('CODEMIRROR_MARKDOWN_JS_URL')
    SHOWDOWN_JS_URL = _get_setting('SHOWDOWN_JS_URL')
    USE_LIVE_PREVIEW = False
