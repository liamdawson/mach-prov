from .apt_get import AptRepositoryAddStateBase, AptPackageInstallStateBase, AptTrustedKeyAddStateBase
import subprocess

class AddMicrosoftKey(AptTrustedKeyAddStateBase):
  """Ensure the Microsoft packages signing key is trusted by apt."""
  name = 'Add Microsoft packages signing key'
  tags = [set(['ubuntu']), set(['debian'])]
  key_name = 'microsoft'

  def signing_key(self):
    pull_key = subprocess.Popen(['curl','-sSL','https://packages.microsoft.com/keys/microsoft.asc'], stdout=subprocess.PIPE)
    dearmored_key = subprocess.check_output(['gpg', '--dearmor'], stdin=pull_key.stdout)
    pull_key.stdout.close()

    return dearmored_key.decode(encoding="utf-8")

class AddVsCodeRepo(AptRepositoryAddStateBase):
  """Ensure the Microsoft VS Code repo is available to apt."""
  name = 'Add Microsoft VS Code repo'
  tags = [set(['ubuntu']), set(['debian'])]
  repo_name = 'vscode'
  repo_url = 'https://packages.microsoft.com/repos/vscode'
  repo_arch = 'amd64'
  repo_version = 'stable'
  repo_repositories = 'main'

class InstallVsCode(AptPackageInstallStateBase):
  """Ensure VS Code (stable) is installed."""
  name = 'Install VS Code'
  tags = [set(['ubuntu']), set(['debian'])]
  packages = ['code']

states = [
  AddMicrosoftKey(),
  AddVsCodeRepo(),
  InstallVsCode()
]
