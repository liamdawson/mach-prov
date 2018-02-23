Import-Module "$PSScriptRoot/Base.psm1" -Force

function Invoke-DeviceUpdate() {
    Invoke-BaseOsUpdate
}

Export-ModuleMember -Function '*'