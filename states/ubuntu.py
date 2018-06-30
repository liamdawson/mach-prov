from .apt_get import PackageInstallStateBase

class DevPackages(PackageInstallStateBase):
  """Ensure preferred dev packages are installed for general dev tasks."""
  name = "Install dev packages"
  packages = [
    'stow',
    'vim'
  ]
  tags = [set(['ubuntu'])]

states = [
  DevPackages()
]
