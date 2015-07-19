require(["base/js/events"], function (events) {
events.on("app_initialized.NotebookApp", function () {
  $('div#header-container').hide();
  $('div#maintoolbar').hide();
});
});