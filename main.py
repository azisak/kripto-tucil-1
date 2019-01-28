from FileInputter import FileInputter, ExtendedFileInputter
from Cipher import VigenereFull, VigenereExtended, Playfair, VigenereStandard, VigenereAutoKey, VigenereRunningKey 
from OutputFormatter import OutputFormatter



if __name__ == "__main__":

  fileReader = ExtendedFileInputter("inputfiles/README.md")
  plaintext = fileReader.getData()

  cipher = VigenereExtended()
  ciphertext = cipher.encrypt(plaintext)
  decryptedCipher = cipher.decrypt(ciphertext)

  # print("Plain text   :", plaintext)l
  # print("Cipher text  :", ciphertext)
  # print("Decipher     :", cipher.decrypt(ciphertext))
  fileReader.safeData("outputfiles/enc_README.md", ciphertext)
  fileReader.safeData("outputfiles/dec_README.md", cipher.decrypt(ciphertext))
  print("Decrypting done")

# if __name__ == "__main__":
  # fileReader = FileInputter("inputfiles/sample.txt")
  # plaintext = fileReader.getText()
  # fmt = OutputFormatter()

  # # print(fmt.originalFormat("!Hesoyam@34","mklunaq"))

  # cipher = VigenereFull(matrixName="test")
  # ciphertext = cipher.encrypt(plaintext)
  # decryptedCipher = cipher.decrypt(ciphertext)

  # print("Plain text   :", plaintext)
  # print("Cipher text  :", ciphertext)
  # print("Decipher     :", cipher.decrypt(ciphertext))
  # print()
  # # print("Decrypted cipher :")
  # z =fmt.originalFormat(plaintext, ciphertext)
  # print("OriginalForma:",z)
  # print("Decipher     :",fmt.originalFormat(z, cipher.decrypt(z)))
  # print()

  # z = fmt.withoutSpacing(plaintext, ciphertext)
  # print("WithoutSpaces:", fmt.withoutSpacing(plaintext, ciphertext))
  # print("Decipher     :",fmt.withoutSpacing(z, cipher.decrypt(z)))
  # print()

  # z = fmt.groupOfNWords(ciphertext)
  # print("GroupOfNWords:", fmt.groupOfNWords(ciphertext))
  # print("Decipher     :",fmt.groupOfNWords(cipher.decrypt(z)))
