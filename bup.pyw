#!python
# coding=utf8
"""non-ascii paths shall be passed to zipfile as they are, i.e. p (in fact, unicode(p));
   however, to print them, encoding shall be done, i.e. p.encode('utf8')
"""

# TODO: test archive after all, if problem then scream, bitch!
# TODO: create gui ¡MORE SWaG!
# TODO: keep settings in %appdata%, so they’ll be buped
# TODO: add only changed or new files
# TODO: ¿profiles? ¡PROBABLY NOT!

import zipfile, os, datetime, itertools

fld1 = unicode(os.path.expanduser('~'))
fld2 = u'D:\\dev\\GitHub'
fld3 = u'D:\\Dropbox\\mine\\notes-md'
dest = 'S:\\bup\\'
dte = '%y-%m-%d-%H-%M'
crap = (u'cache', u'caches', u'Cache', u'Caches',
        u'Chromium',
        u'.gimp-2.8',
        u'AppData\\Local\\GitHub', u'gith..', u'github',
        u'Temporary', u'Temp', u'temp', u'tmp',
        u'Microsoft\\SkyDrive',
        u'Microsoft\\Windows Live\\Contacts',
        u'Microsoft\\Windows\\Explorer',
        u'AppData\\Roaming\\Dropbox',
        u'FastStone\\FSIV',
        u'Firefox\\Crash Reports',
        u'Sublime Text 2\\Backup',
        u'Roaming\\uTorrent',
        u'Roaming\\vlc\\art',
        u'gPodder\\Downloads',
        u'GTA IV\\User Music',
        u'vova\\Downloads'
    )

def do(a):
    for r,d,f in a:
        for c in crap:
            v = True
            if c in r:
                v = False
                break
            else:
                continue
        if v:
            yield (r, d, f)

goodies = do(itertools.chain(os.walk(fld1), os.walk(fld2), os.walk(fld3)))

with zipfile.ZipFile(dest+datetime.datetime.now().strftime(dte)+'.zip', 'w', zipfile.ZIP_DEFLATED) as f:
    for root, dirs, files in goodies:
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