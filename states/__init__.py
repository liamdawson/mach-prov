from . import gnome_shell, apt_get, xps_15, user_shell

states = [] + apt_get.states + xps_15.states + gnome_shell.states + user_shell.states

def relevant_states(tags):
  return filter(lambda state: state.should_apply(tags), states)
