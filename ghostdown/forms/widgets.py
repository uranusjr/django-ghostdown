#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.forms import widgets, Media
from django.template import Context
from django.template.loader import get_template_from_string
from ghostdown.conf import settings


__all__ = ['GhostdownInput']


class GhostdownInput(widgets.HiddenInput):
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
        template = get_template_from_string(GHOSTDOWN_INPUT_TEMPLATE_STRING)
        context = Context({
            'original': original,
            'original_id': original_id,
            'ghostdown_id': ghostdown_id,
            'content': value or '',
        })
        return template.render(context)

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


# Used to render GhostdownInput
GHOSTDOWN_INPUT_TEMPLATE_STRING = """
<div class="features">
  <section class="editor">
    <div class="outer">
      <div class="editorwrap">
        <section class="entry-markdown">
          <section class="entry-markdown-content">
            <textarea id="{{ ghostdown_id }}">{{ content }}</textarea>
          </section>
        </section>
      </div>
    </div>
  </section>
  {{ original|safe }}
</div>
<script>
(function ($, CodeMirror) {
  'use strict';
  $(document).ready(function () {
    var ghostdownTextArea = document.getElementById('{{ ghostdown_id }}');
    if (!ghostdownTextArea)
      return;
    var editor = CodeMirror.fromTextArea(ghostdownTextArea, {
      'mode': 'markdown',
      'tabMode': 'indent',
      'lineWrapping': true
    });
    editor.on("change", function () {
      $('#{{ original_id }}').val(editor.getValue());
    });
  });
}(jQuery, CodeMirror));
</script>
"""
