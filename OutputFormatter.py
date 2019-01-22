

class OutputFormatter:
  def __init__(self):
    pass

  def originalFormat(self, plainText, cipherText): pass
    # TODO: Implement original formatter

  def withoutSpacing(self, text):
    return text.replace(' ','');

  def groupOfNWords(self, text, N=5):
    grouped = " ".join([text[i:i+N] for i in range(0,len(text),N)])
    return grouped
