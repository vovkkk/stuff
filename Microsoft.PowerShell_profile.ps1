﻿. ~\AppData\Local\GitHub\shell.ps1
Push-Location (Split-Path -Path $MyInvocation.MyCommand.Definition -Parent)
Import-Module ~\AppData\Local\GitHub\PoshGit_*\src\posh-git.psd1
function global:prompt {
    $realLASTEXITCODE = $LASTEXITCODE
    # Reset color, which can be messed up by Enable-GitColors
    $Host.UI.RawUI.ForegroundColor = $GitPromptSettings.DefaultForegroundColor
    Write-Host($pwd.ProviderPath) -nonewline
    Write-VcsStatus
    $global:LASTEXITCODE = $realLASTEXITCODE
    return "
> "
}
Pop-Location
Start-SshAgent -Quiet