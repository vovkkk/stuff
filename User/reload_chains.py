import sublime_plugin


class MineReloadChainpluginduh(sublime_plugin.TextCommand):
    def is_enabled(self):
        return self.view.score_selector(0, "text.chain") > 0

    is_visible = is_enabled

    def description(self): return u'Reload Chains plugin'

    def run(self, edit):
        # C:\Users\vova\AppData\Roaming\Sublime Text 2\Packages\Chains\
        sublime_plugin.reload_plugin('C:\\Users\\vova\\AppData\\Roaming\\Sublime Text 2\\Packages\\Chains\\Chains.py')
