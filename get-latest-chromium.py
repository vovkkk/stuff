#!/usr/bin/env python
# coding=utf-8
import os, shutil, urllib2, tempfile, io, zipfile
# TODO: check are we rolling?
# TODO: call me if we ready to roll
# TODO: choose to roll or nah man

class LetUsGetRatchet:
    def run(self):
        cut_da_crap = ['..', 'interactive_ui_tests.exe', '64'] + map(lambda a: str('\\'+a), ('ar.pak', 'bg.pak', 'bn.pak', 'ca.pak', 'cs.pak', 'da.pak', 'de.pak', 'el.pak', 'es.pak', 'es-419.pak', 'et.pak', 'fi.pak', 'fil.pak', 'fr.pak', 'gu.pak', 'he.pak', 'hi.pak', 'hr.pak', 'hu.pak', 'id.pak', 'it.pak', 'ja.pak', 'kn.pak', 'ko.pak', 'lt.pak', 'lv.pak', 'ml.pak', 'mr.pak', 'ms.pak', 'nb.pak', 'nl.pak', 'pl.pak', 'pt-BR.pak', 'pt-PT.pak', 'ro.pak', 'sk.pak', 'sl.pak', 'sr.pak', 'sv.pak', 'ta.pak', 'te.pak', 'th.pak', 'tr.pak', 'uk.pak', 'vi.pak', 'zh-CN.pak', 'zh-TW.pak'))
        got_da_chrome = urllib2.urlopen(urllib2.urlopen('http://download-chromium.appspot.com/dl/Win').geturl()).read()
        grist = tempfile.gettempdir() + '\\chrome-win32.zip'
        with io.open(grist, 'wb') as f:
            f.write(got_da_chrome)
        with zipfile.ZipFile(grist, 'r') as f:
            shutil.rmtree('D:\\Program Files\\inet\\chrome-win32')
            members = self.grind(map(lambda a: ((a, b) for b in cut_da_crap), f.namelist()))
            f.extractall('D:\\Program Files\\inet', members)
        os.remove(grist)

    def grind(self, m):
        for l in m:
            v = True
            for i in l:
                if i[1] in i[0]:
                    v = False
            if v:
                yield i[0]


if __name__ == '__main__':
    LetUsGetRatchet().run()