from .apt_get import AptPackageInstallStateBase

class AptZshState(AptPackageInstallStateBase):
  """"""
  name = 'Install bash and zsh'
  tags = [set('ubuntu'), set('debian')]
  packages = ['bash', 'zsh']

states = [
  AptZshState()
]
