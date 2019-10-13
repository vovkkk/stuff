#!python2
# coding=utf8
import os, shutil, urllib2, tempfile, io, zipfile

install_path = u'D:\\Program Files\\inet\\chrome-win'


class LetUsGetRatchet:
    def yup(self):
        cut_da_crap = ['..', 'interactive_ui_tests.exe'] + map(lambda a: str('/'+a), ('ar.pak', 'bg.pak', 'bn.pak', 'ca.pak', 'cs.pak', 'da.pak', 'de.pak', 'el.pak', 'es.pak', 'es-419.pak', 'et.pak', 'fi.pak', 'fil.pak', 'fr.pak', 'gu.pak', 'he.pak', 'hi.pak', 'hr.pak', 'hu.pak', 'id.pak', 'it.pak', 'ja.pak', 'kn.pak', 'ko.pak', 'lt.pak', 'lv.pak', 'ml.pak', 'mr.pak', 'ms.pak', 'nb.pak', 'nl.pak', 'pl.pak', 'pt-BR.pak', 'pt-PT.pak', 'ro.pak', 'sk.pak', 'sl.pak', 'sr.pak', 'sv.pak', 'ta.pak', 'te.pak', 'th.pak', 'tr.pak', 'uk.pak', 'vi.pak', 'zh-CN.pak', 'zh-TW.pak'))
        got_da_chrome = urllib2.urlopen(urllib2.urlopen('http://download-chromium.appspot.com/dl/Win').geturl()).read()
        grist = tempfile.gettempdir() + '\\chrome-win32.zip'
        with io.open(grist, 'wb') as f:
            f.write(got_da_chrome)
        with zipfile.ZipFile(grist, 'r') as f:
            shutil.rmtree(install_path)
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


class CallMeBro:
    def maybe(self, q):
        import win32ui, win32com.client, subprocess
        if q == 'rolling?':
            for p in win32com.client.GetObject('winmgmts:').InstancesOf('win32_process'):
                if 'chrome' in p.Name:
                    a = win32ui.MessageBox("chrome running\nclose it", "Yo!", 5)
                    if a is 4: pass
                    else: quit()
                    break
        elif q == 'ready':
            a = win32ui.MessageBox("got da new chrome\nstart it?", "Yo!", 1)
            if a is 1:
                subprocess.call(install_path + '\\chrome.exe')
            else: quit()
        else: raise Exception('Bro says "WHA?!!1"')

if __name__ == '__main__':
    CallMeBro().maybe('rolling?')
    LetUsGetRatchet().yup()
    CallMeBro().maybe('ready')
