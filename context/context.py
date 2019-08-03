from yaml import load, CLoader as Loader

def parse(source):
  """
  Parses a valid Context string into a Dict
  """
  # TODO: Expand this to strictly adhere to the Context spec
  return load(source, Loader=Loader)