:: Init Script for cmd.exe
:: Sets some nice defaults
:: Created as part of cmder project

@set "CMDER_ROOT=D:\Program Files\utilities\cmder_mini"
@
@call "%cmder_root%\vendor\lib\lib_base"
@call "%cmder_root%\vendor\lib\lib_path"
@call "%cmder_root%\vendor\lib\lib_console"
@call "%cmder_root%\vendor\lib\lib_git"
@call "%cmder_root%\vendor\lib\lib_profile"

:: Change the prompt style
:: Mmm tasty lamb
::@prompt $E[1;35m$P$S{git}$S$_$E[1;30m{lamb}$S$E[0m

:: Pick right version of clink
@if "%PROCESSOR_ARCHITECTURE%"=="x86" (
    set architecture=86
) else (
    set architecture=64
)

:: Run clink
@"%CMDER_ROOT%\vendor\clink\clink_x%architecture%.exe" inject --quiet --profile "%CMDER_ROOT%\config" --scripts "%CMDER_ROOT%\vendor"

:: Prepare for msysgit

:: I do not even know, copypasted from their .bat
::@set PLINK_PROTOCOL=ssh
:: @if not defined TERM set TERM=cygwin

:: Enhance Path
::@set git_install_root=%CMDER_ROOT%\vendor\msysgit
::@set PATH=%CMDER_ROOT%\bin;%git_install_root%\bin;%git_install_root%\mingw\bin;%git_install_root%\cmd;%git_install_root%\share\vim\vim74;%CMDER_ROOT%;%PATH%

:: Add aliases
::@doskey /macrofile="%CMDER_ROOT%\config\aliases"

:: Set home path
@if not defined HOME set HOME=%USERPROFILE%

@if defined CMDER_START (
    @cd /d "%CMDER_START%"
) else (
    @if "%CD%\" == "%CMDER_ROOT%" (
        @cd /d "%HOME%"
    )
)
