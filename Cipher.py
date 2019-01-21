

class VigenereStandard:
    def __init__(self, key="vigenere"):
        self.key = key.lower()

    def changeKey(self, newKey):
        self.key = newKey.lower()

    def encrypt(self, text):
        text = text.lower()
        text, key = self.__normalizeTextKey(text, self.key)
        text = list(map(lambda p: ord(p) % ord('a'), list(text)))
        key = list(map(lambda p: ord(p) % ord('a'), list(key)))
        cipherText = map(lambda p: chr(
            (p[0] + p[1]) % 26 + ord('a')), zip(text, key))
        cipherText = ''.join(list(cipherText))
        return cipherText

    def decrypt(self, text):
        text = text.lower()
        text, key = self.__normalizeTextKey(text, self.key)
        text = list(map(lambda p: ord(p) % ord('a'), list(text)))
        key = list(map(lambda p: ord(p) % ord('a'), list(key)))
        plainText = map(lambda p: chr(
            (p[0] - p[1]) % 26 + ord('a')), zip(text, key))
        plainText = ''.join(list(plainText))
        return plainText

    def __normalizeTextKey(self, text, key):
        if (text.__len__() == key.__len__()):
            return text, key
        elif (text.__len__() > key.__len__()):
            key = (key * (text.__len__()//key.__len__())) + \
                key[0:text.__len__() % key.__len__()]
            return text, key
        else:  # text.length < key.length
            key = key[0:text.__len__()]
            return text, key
