#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.forms import widgets, Media
from django.template import Context
from django.template.loader import get_template_from_string
from ghostdown.conf import settings
from .templates import GHOSTDOWN_INPUT_TEMPLATE_STRING


__all__ = ['GhostdownInput', 'GHOSTDOWN_INPUT_TEMPLATE_STRING']


class GhostdownInput(widgets.HiddenInput):
    def __init__(self, attrs=None, live_preview=None, value_path=''):
        super(GhostdownInput, self).__init__(attrs)
        if live_preview is None:
            self.live_preview = settings.GHOSTDOWN_USE_LIVE_PREVIEW
        else:
            self.live_preview = live_preview
        if value_path:
            self.value_path = value_path

    def get_template(self):
        return get_template_from_string(GHOSTDOWN_INPUT_TEMPLATE_STRING)

    def render(self, name, value, attrs=None):
        try:
            for k in self.value_path.split('.'):
                value = getattr(value, k)
        except AttributeError:
            pass
        original = super(GhostdownInput, self).render(name, value, attrs)
        original_id = attrs['id']
        ghostdown_feature_id = '{0}_ghosteditor_feature'.format(original_id)
        ghostdown_id = '{0}_ghosteditor_markdown'.format(original_id)
        context = Context({
            'original': original,
            'original_id': original_id,
            'ghostdown_feature_id': ghostdown_feature_id,
            'ghostdown_id': ghostdown_id,
            'content': value or '',
            'live_preview': self.live_preview,
        })
        return self.get_template().render(context)

    @property
    def media(self):
        css = {
            'all': [
                'ghostdown/css/ghostdown.css',
            ]
        }
        js = [
            settings.GHOSTDOWN_JQUERY_URL,
            settings.GHOSTDOWN_CODEMIRROR_JS_URL,
            settings.GHOSTDOWN_CODEMIRROR_MARKDOWN_JS_URL,
            settings.GHOSTDOWN_SHOWDOWN_JS_URL,
            'ghostdown/js/ghostdown.js',
        ]
        if self.live_preview:
            css['all'].append('ghostdown/css/preview.css')
        return Media(css=css, js=[p for p in js if p])
