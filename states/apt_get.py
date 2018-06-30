from .state import State
from sys import stdin, stdout, stderr
import subprocess

def transparent_call(args):
  return subprocess.call(args, stdin=stdin, stdout=stdout, stderr=stderr) == 0

class AptGetUpdate(State):
  """Ensure the apt cache is up to date."""
  name = "apt-get update"
  tags = [
    set(['ubuntu']),
    set(['debian'])
  ]

  def __call__(self):
    return transparent_call(['apt-get', 'update'])

class AptGetUpgrade(State):
  """Ensure the all apt packages are up to date."""
  name = "apt-get upgrade"
  tags = [
    set(['ubuntu']),
    set(['debian'])
  ]

  def __call__(self):
    return transparent_call(['apt-get', 'upgrade', '-y'])

states = [
  AptGetUpdate(),
  AptGetUpgrade()
]

class PackageInstallStateBase(State):
  """Ensure the listed packages are installed."""
  name = "apt-get install"
  packages = []

  def __call__(self):
    result = subprocess.call(['apt-get', 'install', '-y'] + self.packages, stdin=stdin, stdout=stdout, stderr=stderr)

    if result == 0:
      return True
    else:
      return False


class PackageRemoveStateBase(State):
  """Ensure the listed packages are not installed."""
  name = "apt-get remove"
  packages = []

  def __call__(self):
    result = subprocess.call(['apt-get', 'remove', '-y'] + self.packages, stdin=stdin, stdout=stdout, stderr=stderr)

    if result == 0:
      return True
    else:
      return False
