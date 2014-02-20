#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Used to render GhostdownInput
GHOSTDOWN_INPUT_TEMPLATE_STRING = """
<div id="{{ ghostdown_feature_id }}" class="features">
  <section class="editor">
    <div class="outer">
      <div class="editorwrap">
        <section class="entry-markdown">
          <section class="entry-markdown-content">
            <textarea id="{{ ghostdown_id }}">{{ content }}</textarea>
          </section>
        </section>
        {% if live_preview %}
        <section class="entry-preview active">
          <header class="floatingheader">
            &nbsp;&nbsp; Preview <span class="entry-word-count">0 words</span>
          </header>
          <section class="entry-preview-content">
            <div class="rendered-markdown"></div>
          </section>
        </section>
        {% endif %}
      </div>
    </div>
  </section>
  {{ original|safe }}
</div>
<script>
var Ghostdown = {
  featureId: '{{ ghostdown_feature_id }}',
  ghostdownId: '{{ ghostdown_id }}',
  originalId: '{{ original_id }}',
  hasLivePreview: {{ live_preview|yesno:'true,false' }}
};
</script>
"""
