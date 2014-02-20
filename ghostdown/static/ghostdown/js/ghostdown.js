(function ($, CodeMirror, ShowDown) {
  'use strict';
  $(document).ready(function () {
    var ghostdownTextArea = document.getElementById(Ghostdown.ghostdownId);
    if (!ghostdownTextArea)
      return;
    var feature = document.getElementById(Ghostdown.featureId);
    var editor = CodeMirror.fromTextArea(ghostdownTextArea, {
      'mode': 'markdown',
      'tabMode': 'indent',
      'lineWrapping': true
    });

    function updateWordCount() {
      if (!Ghostdown.hasLivePreview)
        return;
      var wordCount = $('.entry-word-count', feature)[0];
      var editorValue = editor.getValue();
      if (editorValue.length) {
        wordCount.innerHTML = editorValue.match(/\S+/g).length + ' words';
      }
    }
    function updatePreview(text) {
      if (!Ghostdown.hasLivePreview)
        return;
      if (typeof(text) == 'undefined')
        text = editor.getValue();
      var preview = $('.entry-preview-content', feature)[0];
      preview.innerHTML = converter.makeHtml(text);
      updateWordCount();
    }

    if (Ghostdown.hasLivePreview)
    {
      var converter = new ShowDown.converter();
      $('.entry-markdown header, .entry-preview header', feature)
      .click(function (e) {
        $('.entry-markdown, .entry-preview', feature).removeClass('active');
        $(e.target).closest('section').addClass('active');
      });
    }

    editor.on('change', function () {
      var text = editor.getValue();
      updatePreview(text);
      $('#' + Ghostdown.originalId).val(text);
    });
    updatePreview(editor.getValue());

    // Sync scrolling
    $('.CodeMirror-scroll', feature).scroll(function (e) {
      // vars
      var $codeViewport = $(e.target);
      var $previewViewport = $('.entry-preview-content', feature);
      var $codeContent = $('.CodeMirror-sizer', feature);
      var $previewContent = $('.rendered-markdown', feature);

      // calc position
      var codeHeight = $codeContent.height() - $codeViewport.height();
      var previewHeight = $previewContent.height() - $previewViewport.height();
      var ratio = previewHeight / codeHeight;
      var previewPostition = $codeViewport.scrollTop() * ratio;

      // apply new scroll
      $previewViewport.scrollTop(previewPostition);

      // Shadow on Markdown if scrolled
      if ($(this).scrollTop() > 10)
        $('.entry-markdown', feature).addClass('scrolling');
      else
        $('.entry-markdown', feature).removeClass('scrolling');
    });

    // Shadow on Preview if scrolled
    $('.entry-preview-content', feature).scroll(function() {
      if ($('.entry-preview-content', feature).scrollTop() > 10)
        $('.entry-preview', feature).addClass('scrolling');
      else
        $('.entry-preview', feature).removeClass('scrolling');
    });
  });
}(jQuery, CodeMirror, Showdown));
