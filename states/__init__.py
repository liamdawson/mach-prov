import gnome_shell
import apt_get
import xps_15

states = reduce(lambda current_states, new_states: current_states + new_states,
[
  apt_get.states,
  xps_15.states,
  gnome_shell.states
], [])

def relevant_states(tags):
  return filter(lambda state: state.should_apply(tags), states)
