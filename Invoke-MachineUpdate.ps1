Param(
    [string]$deviceName
)

Import-Module "$PSScriptRoot/$deviceName" -Force
Invoke-DeviceUpdate