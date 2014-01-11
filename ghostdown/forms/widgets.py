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

    template = get_template_from_string(GHOSTDOWN_INPUT_TEMPLATE_STRING)

    def __init__(self, attrs=None, value_key=''):
        super(GhostdownInput, self).__init__(attrs)
        self.value_key = value_key

    def render(self, name, value, attrs=None):
        if self.value_key:
            for key in self.value_key.split('.'):
                value = getattr(value, key)
        original = super(GhostdownInput, self).render(name, value, attrs)
        original_id = attrs['id']
        ghostdown_id = '{0}_ghosteditor_markdown'.format(original_id)
        context = Context({
            'original': original,
            'original_id': original_id,
            'ghostdown_id': ghostdown_id,
            'content': value or '',
        })
        return self.template.render(context)

    @property
    def media(self):
        css = {
            'all': (
                'ghostdown/css/ghostdown.css',
            )
        }
        js = (
            settings.GHOSTDOWN_JQUERY_URL,
            settings.GHOSTDOWN_CODEMIRROR_JS_URL,
            settings.GHOSTDOWN_CODEMIRROR_MARKDOWN_JS_URL,
        )
        return Media(css=css, js=[p for p in js if p])
