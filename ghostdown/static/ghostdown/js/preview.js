(function ($, ShowDown) {
  'use strict';

  $(document).ready(function () {
    var ghostdownTextArea = document.getElementById(Ghostdown.ghostdownId);
    if (!ghostdownTextArea)
      return;

    var converter = new ShowDown.converter();

    // Really not the best way to do things as it includes Markdown formatting
    // along with words
    function updateWordCount() {
      var wordCount = $('#' + Ghostdown.featureId + ' .ntry-word-count')[0];
      editorValue = editor.getValue();

      if (editorValue.length) {
          wordCount.innerHTML = editorValue.match(/\S+/g).length + ' words';
      }
    }

    function updatePreview() {
        var preview = document.getElementsByClassName('rendered-markdown')[0];
        preview.innerHTML = converter.makeHtml(editor.getValue());

        updateWordCount();
    }
  });
}(jQuery, ShowDown));
