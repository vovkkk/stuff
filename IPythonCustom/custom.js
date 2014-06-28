$([IPython.events]).on("app_initialized.NotebookApp", function () {
  $('div#header').hide();
  $('div#maintoolbar').hide();
});