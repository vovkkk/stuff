#!python
# coding=utf8
"""non-ascii paths shall be passed to zipfile as they are, i.e. p (in fact, unicode(p));
   however, to print them, encoding shall be done, i.e. p.encode('utf8')
"""
import pprint
# TODO: create gui ¡MORE SWaG!
""" gui spec:
    ✔ 3 buttons
        ✔ full Backup       simply create zip from certain paths (current default)
        - partial Backup
          compare crc’s of certain files with crc’s of files from certain zipfiles:
            - for each zip create a dict {fname:crc}
            - file from newer zip replaces crc in dict
        - config
    ✔ list of existed zipfiles with thier sizes
        ✔ when at least one zipfile chosen [partial Backup] button become active
        - if several zipfiles are chosen [partial Backup] is based on them
        - update list after new backup was done
    ✔ self.console to print errors and other useful info
"""
# TODO: keep settings in %appdata%, so they’ll be buped
# TODO: add only changed or new files
# TODO: ¿profiles? ¡PROBABLY NOT!

import zipfile, os, datetime, itertools, zlib, ttk, threading
import Tkinter as tk
import ScrolledText as tkst

class BUP(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.settings()
        self.goodies = itertools.imap(lambda i: self.cut_da_crap(i, self.crap), (os.walk(f) for f in self.what))
        self.createWidgets()
        # self.JesusSaves(goodies)
        # with zipfile.ZipFile(path, 'r') as f:
        #     buped_files = {o.filename: o.CRC for o in f.infolist()}
        # self.saves(self.partial_bup(buped_files, goodies))

    def createWidgets(self):
        self.columnconfigure(4, weight=1)
        self.rowconfigure(2, weight=1)
        self.grid()
        # create
        self.full_bup_btn = ttk.Button(text='Full backup')
        self.part_bup_btn = ttk.Button(text='Partial backup', state='disabled')
        self.config_btn   = ttk.Button(text='Configuration')
        self.dest_tree = ttk.Treeview(columns=(' ',' '))
        self.console = tkst.ScrolledText(font='Consolas 10', wrap=tk.WORD, insertwidth=1, padx=10, pady=5, width=103)
        # place
        for i, b in enumerate([self.full_bup_btn, self.part_bup_btn, self.config_btn], start=1):
            b.grid(row=1, column=i, sticky='w')
        self.dest_tree.grid(row=2, column=1, columnspan=3, sticky='nswe')
        self.console.grid(row=2, column=4, sticky='nswe')
        # bind
        self.full_bup_btn.bind('<Button-1>', self.JesusSaves)
        # self.part_bup_btn.bind('<Button-1>', self.JesusSavesThoseWhoDeserves)
        # self.config_btn.bind('<Button-1>', self.Config)
        self.dest_tree.bind('<<TreeviewSelect>>', self.Activate_part_bup_btn)
        self.fill_treeview()

    def fill_treeview(self):
        bups = [i for i in os.listdir(self.dest) if i.endswith('.zip')]
        sizes = [os.path.getsize(os.path.join(self.dest, f)) for f in bups]
        self.dest_tree.heading("#1", text=u'{0}{2}{1} files'.format(self.dest, len(bups), ' '*4))
        self.dest_tree.heading("#2", text=u'{0} GiB'.format(round(float(reduce(lambda x, y: x+y, sizes))/1024**3, 2)))
        self.dest_tree.column("#0", width=1)
        self.dest_tree.column("#1", width=150)
        self.dest_tree.column("#2", anchor='e', width=70, stretch=False)
        self.months = sorted(list(set(d.strftime('%Y, %B') for d in (datetime.datetime.strptime(f.split('.')[0], self.dte) for f in bups))), key=lambda m: datetime.datetime.strptime(m, '%Y, %B'))
        for i, f in enumerate(self.months, start=1):
            self.dest_tree.insert(parent='', iid=i, index='end', values=[f], open=True, tags=('month'))
        self.dest_tree.tag_configure('month', background='#eee')
        for i, f in enumerate(bups):
            iid = 1 + self.months.index(datetime.datetime.strptime(f.split('.')[0], self.dte).strftime('%Y, %B'))
            self.dest_tree.insert(parent=iid, index='end', values=[f, str(round(float(sizes[i])/1024000, 3)).replace('.', ' ')+' KB'])

    def Activate_part_bup_btn(self, event):
        self.part_bup_btn.state(['!disabled'])
        self.selected_bups = [s for s in (self.dest_tree.set(s, column='#1') for s in self.dest_tree.selection()) if '.zip' in s]

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

    def JesusSaves(self, event):
        self.full_bup_btn.state(['disabled'])
        self.dest_tree.state(['disabled'])
        zip_bup = self.dest+datetime.datetime.now().strftime(self.dte)+'.zip'
        goodies = self.goodies
        def _sender(event_for_wait, event_for_set):
            event_for_wait.wait()
            event_for_wait.clear()
            if event_for_wait is write_event:
                with zipfile.ZipFile(zip_bup, 'w', zipfile.ZIP_DEFLATED) as f:
                    # for g in self.goodies:
                    for root, dirs, files in itertools.chain(*self.goodies):
                        if files: # ignore empty roots, nm, each dir’ll be root eventually
                            for i in files:
                                try:
                                    f.write(os.path.join(root, i))
                                    # self.console.insert(1.0, os.path.join(root, i)+'\n')
                                except Exception as e:
                                    self.console.insert(1.0, str(e)+'\n')
                                    # print e
                                # print(root.encode('utf8'), i.encode('utf8'))
                                # else:
                                #     pass
                        elif not dirs:
                            pass
                            # self.console.insert(1.0, 'Skip empty folder:\n  %s\n\n'%root)
                        else:
                            # print('oops', root, dirs, files)
                            pass
                                    # print root
                            # print 'done'
            else:
                with zipfile.ZipFile(zip_bup, 'r') as f:
                    wha = f.testzip()
                end = datetime.datetime.now()
                self.console.insert(1.0, str(end-start)+'\n\nERRORS IN ZIP_FILE %s\n\n' % wha)
                self.full_bup_btn.state(['!disabled'])
                # re-fill tree
                self.dest_tree.delete(*(i for i in xrange(1, len(self.months)+1)))
                self.fill_treeview()
            event_for_set.set()
        start = datetime.datetime.now()
        write_event = threading.Event()
        report_event = threading.Event()
        t1 = threading.Thread(target=_sender, args=(write_event, report_event))
        t2 = threading.Thread(target=_sender, args=(report_event, write_event))
        t1.start()
        t2.start()
        write_event.set()

    def amen(self, f, root, files):
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

    # def partial_bup(self, buped_files, goodies):
    #     def CRC32_from_file(filename):
    #         buf = open(filename,'rb').read()
    #         return (zlib.crc32(buf) & 0xFFFFFFFF)
    #     for g in goodies:
    #         for root, _, files in g:
    #             for i in files:
    #                 f = os.path.join(root, i)
    #                 try:
    #                     if CRC32_from_file(f) != buped_files[f[3:].replace('\\', '/')]:
    #                         # print CRC32_from_file(f) , buped_files[f[3:].replace('\\', '/')] , '\t', f
    #                         yield f
    #                     else: pass
    #                 except KeyError:
    #                     yield f
    #                 except IOError as e:
    #                     print e

    # def saves(self, goodies):
    #     zip_bup = self.dest+datetime.datetime.now().strftime(self.dte)+'.zip'
    #     with zipfile.ZipFile(zip_bup, 'w', zipfile.ZIP_DEFLATED) as f:
    #         for g in goodies:
    #             f.write(g)

    def settings(self):
        self.what = (unicode(os.path.expanduser('~')),
                u'D:\dev\GitHub',
                u'D:\Dropbox\mine\\notes-md')
        self.dest = 'S:\\bup\\'
        self.dte = '%y-%m-%d-%H-%M'
        self.crap = (
            u'cache', u'Cache', u'Temp', u'tmp', u'.gimp-2.8',
            u'vova\Downloads',
            # apps
            u'AppData\Local\GitHub', u'gith..', u'github',
            u'Local\Mozilla\Firefox',  u'Chromium',
            u'Firefox\Crash Reports', u'AppData\Local\Mozilla\\updates',
            u'AppData\Roaming\Dropbox',
            u'Roaming\Yandex\YandexDisk',
            u'gPodder\Downloads',
            u'Roaming\\uTorrent',
            u'AppData\Roaming\Zona\plugins',
            u'FastStone\FSIV',
            u'Roaming\\vlc\\art',
            u'Sublime Text 2\Backup',
            u'GTA IV\\User Music',
            u'zeal\docsets',
            u'AppData\Local\Texts',
            u'TuneUp Utilities\CrashDumps',
            u'AppData\Local\Arcode',
            u'AppData\Local\Mailbird',
            u'.VirtualBox',
            # ms
            u'\AC\Microsoft',
            u'LocalState',
            u'Microsoft\SkyDrive',
            u'Microsoft\Windows Live\Contacts',
            u'Microsoft\Windows\Explorer',
            u'Local\Microsoft\Windows\\Notifications',
            u'Local\Microsoft\Windows\WER\ReportArchive',
            u'Local\Microsoft\Windows\WER\ReportQueue',
            u'Local\Microsoft\Windows\SkyDrive\logs',
            u'Local\Microsoft\Windows\PowerShell\CommandAnalysis',
            u'Local\Microsoft\Messenger',
            u'Local\Microsoft\Media Player',
            u'Local\Microsoft\WLSetup'
            )

if __name__ == '__main__':
    BUP().mainloop()