class FileInputter:

  def __init__(self, file_path):
    try:
      self.fp = open(file_path)
    except:
      print("Something wrong..")

  def getText(self):
    return self.fp.read()
