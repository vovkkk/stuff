#! python2 -u
# coding: utf8
# from __future__ import print_function
import os, time

import yaml, io
with io.open(os.path.join(os.getenv('APPDATA'), u'MySettings.yaml'), 'r', encoding='utf8') as f:
    grist = yaml.load(f).get('news_cache').replace('/', os.sep)

now   = time.time()
stuff = os.listdir(grist)
date  = '%y-%m-%d-%H-%M'
size, amount, errors, newest, files = 0, 0, [], [], []


def fop(files):
    import ctypes
    from ctypes.wintypes import HWND, UINT, LPCWSTR, BOOL

    class SHFILEOPSTRUCTW(ctypes.Structure):
        _fields_ = [
            ("hwnd", HWND),
            ("wFunc", UINT),
            ("pFrom", LPCWSTR),
            ("pTo", LPCWSTR),
            ("fFlags", ctypes.c_uint),
            ("fAnyOperationsAborted", BOOL),
            ("hNameMappings", ctypes.c_uint),
            ("lpszProgressTitle", LPCWSTR),
            ]
    SHFileOperationW = ctypes.windll.shell32.SHFileOperationW
    SHFileOperationW.argtypes = [ctypes.POINTER(SHFILEOPSTRUCTW)]
    pFrom = u'\x00'.join(files) + u'\x00'
    args  = SHFILEOPSTRUCTW(wFunc  = UINT(3),
                            pFrom  = LPCWSTR(pFrom),
                            pTo    = None,
                            fFlags = 64,
                            fAnyOperationsAborted = BOOL())
    out = SHFileOperationW(ctypes.byref(args))

each_ten = range(10, len(stuff), 10)
len_stuff = len(stuff)

for i, f in enumerate(stuff, start=1):
    f = os.path.join(grist, f)
    try:
        modified = os.path.getmtime(f)
    except Exception as e:
        errors.append(str(e))
    else:
        if int(now-modified) > 2592000:
            amount += 1
            size   += os.path.getsize(f)
            newest.append(time.gmtime(modified))
            files.append(f)
    # if i in each_ten:
        # calling cls is very slow on each file, so reduce to each tenth
        # subprocess.call(['cls'], shell=True)
    msg = 'scand %d out of %d files' % (i, len_stuff) + ('; to remove %d files (%.2f MiB)' % (amount, size/float(1024**2)) if amount else '')
    print msg + chr(8)*(len(msg)+1),

sorted(newest)

print
print('%d / %d' % (amount, len(stuff)))
print('%.2f MiB' % (size/float(1024**2)))
print([time.strftime(date, newest[0]), time.strftime(date, newest[~0])])
print(u'\n'.join(errors))

if files:
    fop(files)

input('press <enter>')
