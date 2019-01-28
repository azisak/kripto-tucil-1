class FileInputter:

  def __init__(self, file_path):
    try:
      self.fp = open(file_path)
    except:
      print("Something wrong..")

  def getText(self):
    return self.fp.read()

class ExtendedFileInputter:
  def __init__(self, file_path):
    try:
      self.fp = open(file_path, "rb")
    except:
      print("Something wrong..")

  def getData(self):
    return self.fp.read()

  def safeData(self,path, data):
    binary_file = open(path, "wb")
    binary_file.write(data)
    binary_file.close()
