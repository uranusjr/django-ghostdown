#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.functional import curry
try:
    # Django 1.7 and onwards.
    from django.utils.module_loading import import_string
except ImportError:
    # Older version of Django. This is deprecated now, and you should upgrade
    # Django asap!
    from django.utils.module_loading import import_by_path
    import_string = import_by_path
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_render_func():
    renderer_info = settings.GHOSTDOWN_MARKDOWN_RENDERER
    if 'path' not in renderer_info:
        raise ImproperlyConfigured(
            'Could not import markdown renderer. "path" value missing from '
            'settings.'
        )
    func = import_string(renderer_info['path'])
    return curry(func, *renderer_info['args'], **renderer_info['kwargs'])
