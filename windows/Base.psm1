function Invoke-BaseOsUpdate() {
    # disable system sleep configuration
    powercfg.exe -x -monitor-timeout-ac 0
    powercfg.exe -x -monitor-timeout-dc 0
    powercfg.exe -x -disk-timeout-ac 0
    powercfg.exe -x -disk-timeout-dc 0
    powercfg.exe -x -standby-timeout-ac 0
    powercfg.exe -x -standby-timeout-dc 0
    powercfg.exe -x -hibernate-timeout-ac 0
    powercfg.exe -x -hibernate-timeout-dc 0
    powercfg.exe /hibernate off

    # set execution policy to allow scripts
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

    # ensure powershell help is downloaded
    Update-Help
}

Export-ModuleMember -Function '*'