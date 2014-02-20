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
var Ghostdown = {
  ghostdownId: '{{ ghostdown_id }}',
  originalId: '{{ original_id }}'
};
</script>
"""
