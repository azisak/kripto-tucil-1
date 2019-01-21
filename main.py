from FileInputter import FileInputter
from Cipher import VigenereStandard, ViginereAutoKey, ViginereRunningKey, Playfair

if __name__ == "__main__":
  fileReader = FileInputter("inputfiles/sample.txt")
  plaintext = fileReader.getText()

  cipher = Playfair("jalanganeshasepuluh")
  ciphertext = cipher.encrypt(plaintext)

  print("Plain text : ", plaintext)
  print("Cipher text : ", ciphertext)
  # print("Decrypted cipher : ",cipher.decrypt(ciphertext))
