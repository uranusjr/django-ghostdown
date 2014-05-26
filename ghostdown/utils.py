#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from importlib import import_module
from django.utils.functional import curry
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_render_func():
    renderer_info = settings.GHOSTDOWN_MARKDOWN_RENDERER
    if 'path' not in renderer_info:
        raise ImproperlyConfigured(
            'Could not import markdown renderer. "path" value missing from '
            'settings.'
        )
    try:
        modulename, funcname = renderer_info['path'].rsplit('.')
        func = getattr(import_module(modulename), funcname)
    except:
        raise ImproperlyConfigured(
            'Could not import markdown renderer "{path}". Setting '
            '"GHOSTDOWN_MARKDOWN_RENDERER" should be a dot-seperated import '
            'path to a function.'.format(path=renderer_info['path'])
        )
    return curry(func, *renderer_info['args'], **renderer_info['kwargs'])
