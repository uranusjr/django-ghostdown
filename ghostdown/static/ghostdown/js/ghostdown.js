(function ($, CodeMirror) {
  'use strict';
  $(document).ready(function () {
    var ghostdownTextArea = document.getElementById(Ghostdown.ghostdownId);
    console.log(Ghostdown.ghostdownId);
    if (!ghostdownTextArea)
      return;
    var editor = CodeMirror.fromTextArea(ghostdownTextArea, {
      'mode': 'markdown',
      'tabMode': 'indent',
      'lineWrapping': true
    });
    editor.on("change", function () {
      $('#' + Ghostdown.originalId).val(editor.getValue());
    });
  });
}(jQuery, CodeMirror));
