

class OutputFormatter:
  def __init__(self):
    pass

  def originalFormat(self, plainText, cipherText): 
    text = list(plainText)
    cpr = list(cipherText)
    text = [cpr.pop(0) if c.isalpha() else c for c in text]
    return "".join(text)

  def withoutSpacing(self, plainText, cipherText):
    text = self.originalFormat(plainText, cipherText)
    return text.replace(' ','');

  def groupOfNWords(self, text, N=5):
    grouped = " ".join([text[i:i+N] for i in range(0,len(text),N)])
    return grouped
