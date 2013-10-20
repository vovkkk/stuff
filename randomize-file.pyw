#!/usr/bin/python
# -*- coding: utf-8 -*-
# Opens random file from specific folder in default application
# Python 2.1.1 licence http://www.python.org/2.1.1/license.html

# TODO: exclude subfolders
# TODO: keybindings??
# TODO: optionally - take all files from subfolders

import os, random, webbrowser
from Tkinter import *

folder = os.path.expanduser('~/Pictures')
all_files = []

def LoadFolder(folder):
    global all_files
    path.set(folder)
    all_files = os.listdir(folder)

def ChooseFolder(event):
    global folder, all_files
    import tkFileDialog
    folder = tkFileDialog.askdirectory(initialdir=folder)
    LoadFolder(folder)
    OpenFile(all_files)

def PasteText(event):
    global folder, all_files
    import win32clipboard
    win32clipboard.OpenClipboard()
    folder = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    LoadFolder(folder)
    OpenFile(all_files)

def ClickGo(event):
    global all_files
    OpenFile(all_files)

def OpenFile(all_files):
    random_file = all_files[random.randint(0, len(all_files)) - 1]
    webbrowser.open(folder + "/" + random_file)

root = Tk()
root.wm_attributes("-topmost", 1)

path = StringVar()
path.set('LMB to choose folder, RMB to paste from clipboard')
entry = Entry(textvariable=path, width=len(path.get()))
entry.bind("<Button-1>", ChooseFolder)
entry.bind("<Button-3>", PasteText)
entry.pack(anchor='w', expand='yes', fill='both', side='left')

btn_go = Button(root, text = 'Go!')
btn_go.bind("<Button-1>", ClickGo)
btn_go.pack(anchor='se',side='right')

root.mainloop()