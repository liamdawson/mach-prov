from .state import State
from sys import stdin, stdout, stderr
import platform
import subprocess

def transparent_call(args):
  return subprocess.call(args, stdin=stdin, stdout=stdout, stderr=stderr) == 0

class UbuntuAptMirrors(State):
  """Ensure the preferred Ubuntu apt mirror is used."""
  name = "Select preferred APT mirror"
  tags = [set(['ubuntu'])]

  def __call__(self, state_data):
    preferred_mirror = state_data['apt_mirror']

    apt_conf = """
# set by provision.py

deb {mirror} {codename} main restricted universe multiverse
deb {mirror} {codename}-security main restricted universe multiverse
deb {mirror} {codename}-updates main restricted universe multiverse
deb {mirror} {codename}-backports main restricted universe multiverse
    """.format(mirror=preferred_mirror, codename=platform.linux_distribution()[2])

    with open('/etc/apt/sources.list.new', 'w') as file:
      file.write(apt_conf)

    return transparent_call(['mv', '/etc/apt/sources.list.new', '/etc/apt/sources.list'])

class AptGetUpdate(State):
  """Ensure the apt cache is up to date."""
  name = "apt-get update"
  tags = [
    set(['ubuntu']),
    set(['debian'])
  ]

  def __call__(self, _):
    return transparent_call(['apt-get', 'update'])

class AptGetUpgrade(State):
  """Ensure the all apt packages are up to date."""
  name = "apt-get upgrade"
  tags = [
    set(['ubuntu']),
    set(['debian'])
  ]

  def __call__(self, _):
    return transparent_call(['apt-get', 'upgrade', '-y'])

class AptPackageInstallStateBase(State):
  """Ensure the listed packages are installed."""
  name = "apt-get install"
  packages = []

  def __call__(self, _):
    result = subprocess.call(['apt-get', 'install', '-y'] + self.packages, stdin=stdin, stdout=stdout, stderr=stderr)

    if result == 0:
      return True
    else:
      return False

class AptPackageRemoveStateBase(State):
  """Ensure the listed packages are not installed."""
  name = "apt-get remove"
  packages = []

  def _check_installed(self, packages):
    package_list = subprocess.check_output(['dpkg', '--get-selections'] + packages, stderr=None)
    return package_list.splitlines()

  def __call__(self, _):
    installed_packages = self._check_installed(self.packages)

    if any(installed_packages):
      return transparent_call(['apt-get', 'remove', '-y'] + self.packages)
    else:
      print(" * none of the packages were installed, skipping removal.")
      return True

class AptTrustedKeyAddStateBase(State):
  """Ensure the appropriate GPG key is trusted by apt"""

  def _write_signing_key(self, identifier, key):
    with open('/etc/apt/trusted.gpg.d/{}.gpg'.format(identifier), 'wb') as file:
      file.truncate()
      file.write(key)

  def __call__(self, _):
    try:
      self._write_signing_key(self.key_name, self.signing_key())
      return True
    except AttributeError as e:
      print("required attribute not found")
      print(e)
      return False

class AptRepositoryAddStateBase(State):
  """Ensure the provided repo is available to apt"""

  def _write_repo_definition(self, identifier, url, version, repos, arch=None):
    with open('/etc/apt/sources.list.d/{}.list'.format(identifier), 'w') as file:
      file.truncate()
      file.write('deb ')
      if arch:
        file.write('[arch={}] '.format(arch))
      file.write('{} {} {}'.format(url, version, repos))

  def __call__(self, _):
    try:
      self._write_repo_definition(self.repo_name, self.repo_url, self.repo_version, self.repo_repositories, getattr(self, 'repo_arch', None))
      return True
    except AttributeError as e:
      print("required attribute not found")
      print(e)
      return False

class EnsureAptResources(AptPackageInstallStateBase):
  """Ensure the HTTPS transport for apt, and gpg, are available."""
  name = 'Install https apt transport and gpg'
  tags = [set('ubuntu'), set('ubuntu')]
  packages = [
    'apt-transport-https',
    'gpg'
  ]

states = [
  UbuntuAptMirrors(),
  AptGetUpdate(),
  AptGetUpgrade(),
  EnsureAptResources()
]
