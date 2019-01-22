

class OutputFormatter:
  def __init__(self):
    pass

  def originalFormat(self, plainText, cipherText): 
    words = plainText.split(' ')
    cwords = []
    i = 0
    for w in words:
      cwords += [cipherText[i:i+len(w)]]
      i+=len(w)
    cwords = ' '.join(cwords)
    cwords = [cwords[i].upper() if plainText[i].isupper() else cwords[i].lower()  for i in range(len(plainText))]
    return ''.join(cwords)


  def withoutSpacing(self, text):
    return text.replace(' ','');

  def groupOfNWords(self, text, N=5):
    grouped = " ".join([text[i:i+N] for i in range(0,len(text),N)])
    return grouped
