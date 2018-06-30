if 'basestring' not in globals():
  basestring = str

class State:
  def should_apply(self, tags):
    try:
      return any([tags.issuperset(the_set) for the_set in self.tags])
    except AttributeError:
      return False
  
  def __call__(self):
    raise NotImplementedError("State call not implemented for {}".format(self.__class__.__name__))

  def __str__(self):
    name = getattr(self, 'name', self.__class__.__name__)
    description = self.__class__.__doc__ or "No description."

    return "{}\n{}".format(name, description)
