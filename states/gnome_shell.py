from sets import Set
from apt_get import PackageInstallStateBase, PackageRemoveStateBase


class GnomeShellPackage(PackageInstallStateBase):
  """Ensure the Gnome Shell package is installed on this system."""
  name = "Install gnome-shell"
  packages = ['gnome-shell']
  tags = [Set(['ubuntu'])]


class RemoveUbuntuShellPackage(PackageRemoveStateBase):
  """Ensure the Ubuntu Shell package is not installed on this system."""
  name = "Remove ubuntu-shell"
  packages = ['ubuntu-shell']
  tags = [Set(['ubuntu'])]


states = [
  GnomeShellPackage(),
  RemoveUbuntuShellPackage()
]
