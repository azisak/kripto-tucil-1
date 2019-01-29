

class OutputFormatter:
  def __init__(self): pass

class Original(OutputFormatter):
  def format(self, originalText, encodedText):
    text = list(originalText)
    cpr = list(encodedText)
    text = [cpr.pop(0) if c.isalpha() else c for c in text]
    return "".join(text)

class NoSpaces(OutputFormatter):
  def format(self, originalText, encodedText):
    text = list(originalText)
    cpr = list(encodedText)
    text = [cpr.pop(0) if c.isalpha() else c for c in text]
    text = "".join(text)
    return text.replace(' ','')

class GroupOfWords(OutputFormatter):
  def format(self, originalText, encodedText):
    N = 5
    return " ".join([encodedText[i:i+N] for i in range(0,len(encodedText),N)])
    

