#algorithm
'''
class UniqueChars(object):
  def has_unique_chars(self, string):
    #algo1: implmentation set and length comparison
    if string is None:
      return False
    return len(set(string)) == len(string)

  def has_unique_chars(self, string):
    #algo2: hash map lookup
    if string is None:
      return False
    chars_set = set()
    for char in string:
      if char in chars_set:
        return False
      else:
        chars_set.add(char)
    return True

  def has_unique_chars(self, string):
    if string is None:
      return False
    for char in string:
      if string.count(char) > 1:
        return False
    return True


string = 'This fun'    
SS = UniqueChars()
print(SS.has_unique_chars(string))
'''
class UniqueCharsSet(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)

class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        chars_set = set()
        for char in string:
            if char in chars_set:
                return False
            else:
                chars_set.add(char)
        return True
    
class UniqueCharsInPlace(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True


