import sublime, sublime_plugin

ST3 = int(sublime.version()) > 2999

if ST3:
    from Default.sort import permute_lines
else:
    from sort import permute_lines

import ctypes
import functools


def StrCmpLogicalW(s1, s2):
    '"Art", "Wasa", "Älg", "Ved"'
    return ctypes.windll.shlwapi.StrCmpLogicalW(s1, s2)


def logical_sort(text):
    if ST3:
        return sorted(text, key=functools.cmp_to_key(StrCmpLogicalW))
    else:
        return sorted(text, cmp=StrCmpLogicalW)


class SortLinesLogically(sublime_plugin.TextCommand):
    '''using Windows natural sorting'''
    def run(self, edit):
        if sublime.platform() != 'windows':
            return sublime.error_message('Move along, peasant')
        permute_lines(logical_sort, self.view, edit)
