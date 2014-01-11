#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
