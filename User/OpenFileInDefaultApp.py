import sublime_plugin, webbrowser
class OpenFileInDefaultAppCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        if filename is None: self.view.run_command('pandoc_render')
        else: webbrowser.open_new_tab(filename)