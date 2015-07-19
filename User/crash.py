# coding: utf8
import sublime, sublime_plugin, random


class Freeze(sublime_plugin.TextCommand):
    '''
    view.run_command('freeze')
    '''
    def run(self, edit):
        a = u'\n\t'.join([self.line(40) for _ in range(1000)])
        self.view.insert(edit, 0, a)
        start = 0
        eof   = self.view.size()
        step  = 6
        results = []
        for line in self.view.lines(sublime.Region(0, eof)):
            start = 0
            while (start+step) < eof:
                end = start + 6
                item = sublime.Region(start, end)
                text = self.view.substr(item).lstrip()
                results.append(text)
                start = end
        print(results)
        print(len(results))

    def line(self, size):
        return u''.join(random.SystemRandom().choice(u'.фризанисублиме¹²³$‰↑∞←→—≠®™') for _ in range(size))
