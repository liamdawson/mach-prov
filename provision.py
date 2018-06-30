from argparse import ArgumentParser
from importlib import import_module

import states

state_config = {
  'apt_mirror': 'http://mirror.as24220.net/pub/ubuntu/'
}

def format_state_output(state):
  return str(state)

if __name__ == '__main__':
  parser = ArgumentParser(description='Provision machine to meet desired state.')
  parser.add_argument('tags', metavar='TAG', nargs='+', help='State tags to apply (e.g. "ubuntu", "xps15").')
  parser.add_argument('--apply', help='Apply states, rather than listing states to apply.', action='store_true')

  args = parser.parse_args()

  actions = states.relevant_states(set([tag.lower() for tag in args.tags]))

  if args.apply:
    for action in actions:
      print(format_state_output(action))
      if not action(state_config):
        print("Previous action failed. Exiting.")
        break
  else:
    action_list = "\n\n".join(map(format_state_output, actions))
    print("States to apply:\n\n{}".format(action_list))
