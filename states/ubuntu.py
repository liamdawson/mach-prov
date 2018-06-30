from .apt_get import AptPackageInstallStateBase

class UbuntuDevPackages(AptPackageInstallStateBase):
  """Ensure preferred dev packages are installed for general dev tasks."""
  name = "Install dev packages"
  packages = [
    'stow',
    'vim',
    'git',
    'build-essential',
    'w3m',
    'cmake',
    'gdb'
  ]
  tags = [set(['ubuntu'])]

class UbuntuVanityPackages(AptPackageInstallStateBase):
  """Ensure preferred vanity packages are installed for general use."""
  name = "Install vanity packages"
  packages = [
    'fonts-roboto',
    'fonts-noto'
  ]
  tags = [set(['ubuntu'])]
 
states = [
  UbuntuDevPackages(),
  UbuntuVanityPackages()
]
