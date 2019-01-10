'''
def validate(name):
  if len(name) < 10:
    raise ValueError
'''

class NameTooShortError(ValueError):
  pass

def validate(name):
  if len(name) < 10:
    raise NameTooShortError(name)

    
