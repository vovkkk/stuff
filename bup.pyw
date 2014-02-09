#!python
# coding=utf8
"""non-ascii paths shall be passed to zipfile as they are, i.e. p (in fact, unicode(p));
   however, to print them, encoding shall be done, i.e. p.encode('utf8')
"""

# TODO: create gui ¡MORE SWaG!
# TODO: keep settings in %appdata%, so they’ll be buped
# TODO: add only changed or new files
# TODO: ¿profiles? ¡PROBABLY NOT!

import zipfile, os, datetime, itertools
# import Tkinter as tk

class BUP():
    def init(self):
        what = (unicode(os.path.expanduser('~')),
                u'D:\\dev\\GitHub',
                u'D:\\Dropbox\\mine\\notes-md')
        self.dest = 'S:\\bup\\'
        self.dte = '%y-%m-%d-%H-%M'
        crap = (u'cache', u'Cache', u'Temp', u'temp', u'tmp', u'.gimp-2.8',
                u'Local\Mozilla\Firefox',  u'Chromium',
                u'AppData\\Local\\GitHub', u'gith..', u'github',
                u'AppData\\Roaming\\Dropbox',
                u'Microsoft\\SkyDrive',
                u'Microsoft\\Windows Live\\Contacts',
                u'Microsoft\\Windows\\Explorer',
                u'FastStone\\FSIV',
                u'Firefox\\Crash Reports',
                u'Sublime Text 2\\Backup',
                u'Roaming\\uTorrent',
                u'Roaming\\vlc\\art',
                u'gPodder\\Downloads',
                u'GTA IV\\User Music',
                u'vova\\Downloads',
                u'zeal\\docsets')
        goodies = itertools.imap(lambda i: self.cut_da_crap(i, crap), (os.walk(f) for f in self.what))
        self.JesusSaves(goodies)

    def cut_da_crap(self, shit, crap):
        for r,d,f in shit:
            for c in crap:
                v = True
                if c in r:
                    v = False
                    break
                else:
                    continue
            if v:
                yield (r, d, f)

    def JesusSaves(self, goodies):
        zip_bup = self.dest+datetime.datetime.now().strftime(self.dte)+'.zip'
        with zipfile.ZipFile(zip_bup, 'w', zipfile.ZIP_DEFLATED) as f:
            def _amen(root, files):
                if files: # ignore empty roots, nm, each dir’ll be root eventually
                    for i in files:
                        try:
                            f.write(os.path.join(root, i))
                        except Exception as e:
                            print e
                        # print(root.encode('utf8'), i.encode('utf8'))
                else:
                    pass
                    # print('oops', root, dirs, files)
            for g in goodies:
                for root, _, files in g:
                    _amen(root, files)
        with zipfile.ZipFile(zip_bup, 'r') as f:
            wha = f.testzip()
            print('ERRORS IN ZIP_FILE',wha)

if __name__ == '__main__':
    BUP().init()