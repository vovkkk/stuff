Small things (deserves no own repo) goes here.

# For Sublime Text
- **\#1. LAZY colour scheme with highlighting for Diff syntax**.  
    It can be used with Sublime Text and [supposedly] Texmate.  
    The pure beauty:  
    [![](http://storage7.static.itmages.ru/i/13/0608/h_1370707407_2730244_fb28f528b6.png)](http://storage7.static.itmages.ru/i/13/0608/h_1370707407_2730244_fb28f528b6.png)
    - Installation for ST2:
        - put `LAZY.tmTheme` file to `%appdata%\Sublime Text 2\Packages\User`;
        - choose the theme in the app `Preferences > Color Scheme > User > LAZY`.
- **\#2. My personal settings and keybindings for Sublime Text 2**.

    | | |
    | ---: | --- |
    | `f1` | toggle line numbers |
    | `f2` | convert and preview markdown to html via pandoc |
    | `f3` | fold with regex |
    | `f11` | toggle side bar |
    | `f12` | open [File Browser](https://sublime.wbond.net/packages/FileBrowser) |
    | `alt+f1` | search selection in [Zeal](http://zealdocs.org/) |
    | `shift+f1` | search in [Zeal](http://zealdocs.org/) |
    | `shift+backspace` | close file |
    | `alt+1…9` | fold by level 1…9 |
    | `alt+0` | unfold all |
    | `ctrl+shift+.` | increase heading level of a line in mardown file |
    | `ctrl+shift+,` | decrease heading level of a line in mardown file |

- **\#3. Fork of [tasks-OF](https://github.com/poritsky/PlainTasksOF) colour scheme for PlainTasks**.
- **~~\#4. private~~**
- **\#5. OpenFileInDefaultApp.py** (can be used to preview markdown).

# Random stuff
- **\#6. GitHub-akin html template for Pandoc**.
- **\#7. Python script `randomize-file`** (_Windows-only_) opens random file from specific folder in default application.  
    [![](http://storage7.static.itmages.com/i/13/1020/h_1382288778_9465968_6ccfac0d37.png)](http://storage7.static.itmages.com/i/13/1020/h_1382288778_9465968_6ccfac0d37.png)
- **\#8. PowerShell profile** ([GitHub](http://windows.github.com/), two lines for path and input) goes to `%userprofile%\Documents\WindowsPowerShell`.
- **\#9.** `init.bat`:  
        reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /t REG_EXPAND_SZ /d "%"USERPROFILE"%\init.cmd" /f
- **\#10. Python script `get-latest-chromium`** (_Windows-only_) downloads and unpack [‘the raw build of Chromium for Windows, right off the trunk’](https://download-chromium.appspot.com/).
- **\#11. Custom styles for [Brief](http://brief.mozdev.org/) 1.7.x and 2.2.x** make wrap for:
    - headers in headlines view — so even the longest headers are always readable without unfolding;
    - images — so even the widest pics ain’t no spawn horisontal scrolling.
    - Also sets font to the most elegant one on Windows — Segoe UI — the best readability ever.
- **\#12. Custom stuff for [IPython Notebook](http://ipython.org/notebook.html)** — 1) hide toolbar by default and 2) more Windows8-ish overall look — goes to `%userprofile%\.ipython\profile_default\static\custom`.
