#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
from django.conf import settings
from django.forms import widgets, Media
from django.template import Context
from django.template.loader import get_template_from_string
from .templates import GHOSTDOWN_INPUT_TEMPLATE_STRING


__all__ = [
    'GhostdownInput', 'GhostdownHiddenInput',
    'GHOSTDOWN_INPUT_TEMPLATE_STRING',
]


class GhostdownWidgetMixin(widgets.Widget):
    def __init__(self, attrs=None, value_path=''):
        super(GhostdownWidgetMixin, self).__init__(attrs)
        if value_path:
            self.value_path = value_path

    def resolve_value(self, value):
        try:
            for k in self.value_path.split('.'):
                value = getattr(value, k)
        except AttributeError:
            pass
        return value

    def render(self, name, value, attrs=None):
        value = self.resolve_value(value)
        return super(GhostdownWidgetMixin, self).render(name, value, attrs)


class GhostdownHiddenInput(GhostdownWidgetMixin, widgets.HiddenInput):
    pass


class GhostdownInput(GhostdownHiddenInput):
    def __init__(self, attrs=None, live_preview=None, value_path='',
                 codemirror_options=None):
        super(GhostdownInput, self).__init__(attrs, value_path)
        if live_preview is None:
            self.live_preview = settings.GHOSTDOWN_USE_LIVE_PREVIEW
        else:
            self.live_preview = live_preview
        if codemirror_options is None:
            codemirror_options = settings.GHOSTDOWN_CODEMIRROR_DEFAULT_OPTIONS
        self.codemirror_options = codemirror_options

    def get_template(self):
        return get_template_from_string(GHOSTDOWN_INPUT_TEMPLATE_STRING)

    def render(self, name, value, attrs=None):
        value = self.resolve_value(value)
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
            'codemirror_options': json.dumps(self.codemirror_options),
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
