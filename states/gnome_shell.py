from .apt_get import AptPackageInstallStateBase, PackageRemoveStateBase


class GnomeShellPackage(AptPackageInstallStateBase):
  """Ensure the Gnome Session package is installed on this system."""
  name = "Install gnome-session"
  packages = ['gnome-session']
  tags = [set(['ubuntu'])]


class RemoveUbuntuShellPackage(PackageRemoveStateBase):
  """Ensure the Ubuntu Shell package is not installed on this system."""
  name = "Remove ubuntu-session"
  packages = ['ubuntu-session']
  tags = [set(['ubuntu'])]


states = [
  GnomeShellPackage(),
  RemoveUbuntuShellPackage()
]
