from FileInputter import FileInputter
from Cipher import VigenereStandard, ViginereAutoKey, ViginereRunningKey, Playfair
from OutputFormatter import OutputFormatter

if __name__ == "__main__":
  fileReader = FileInputter("inputfiles/sample.txt")
  plaintext = fileReader.getText()
  fmt = OutputFormatter()

  cipher = Playfair("jalanganeshasepuluh")
  ciphertext = cipher.encrypt(plaintext)
  decryptedCipher = cipher.decrypt(ciphertext)

  print("Plain text :", plaintext)
  print("Cipher text :", ciphertext)
  print("Decrypted cipher :")
  # print("\tOriginalFormat:",fmt.)
  print("\tWithoutSpaces:", fmt.withoutSpacing(decryptedCipher))
  print("\tGroupOfNWords:", fmt.groupOfNWords(decryptedCipher))
