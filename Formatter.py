

class Format:
  ORIGINAL = 1
  NO_SPACE = 2
  GROUP = 3
  def format(self): pass
  def create(self, type=None):
    if (type == self.ORIGINAL):
      return Original()

class Original(Format):
  def format(self, text):
    return text.lower()

class NoSpace(Format):
  def format(self, text):
    return "".join(text.split(" "))

class Group(Format):
  def format(self, text):
    return "".join([x for x in text.lower() if x.isalpha()])
