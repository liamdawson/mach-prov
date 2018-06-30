from state import State
from apt_get import PackageInstallStateBase


class BumblebeeNvidiaGraphics(PackageInstallStateBase):
  """Ensure the bumblebee packages are installed for optimal graphics."""
  name = "Install bumblebee-nvidia"
  packages = [
    'bumblebee',
    'bumblebee-nvidia',
    'primus',
    'linux-headers-generic'
  ]
  tags = [set(['ubuntu', 'xps15'])]


states = [
  BumblebeeNvidiaGraphics()
]
