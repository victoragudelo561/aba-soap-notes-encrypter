import base64
import os

from dotenv import load_dotenv
from Crypto.Cipher import AES

load_dotenv()

class AESCipher:
    def __init__(self):
        self.derived_key = base64.b64decode(os.environ['DERIVED_KEY'])
        self.iv = os.environ['IV']
        self.bs = AES.block_size

    def encrypt(self, raw_text):
        padded_raw = self._pad(raw_text)
        cipher = AES.new(self.derived_key, AES.MODE_CBC, self.iv.encode())
        return base64.b64encode(cipher.encrypt(padded_raw.encode())).decode()

    def decrypt(self, encoded_text):
        text_decoded = base64.b64decode(encoded_text)
        cipher = AES.new(self.derived_key, AES.MODE_CBC, self.iv.encode())
        return self._unpad(cipher.decrypt(text_decoded))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])].decode()

prueba = AESCipher()

print(prueba.decrypt("w5FRqcWxQv3AOoSTFTk4OclWoDbQjdsnL74ms/o/Ef0OYQ99kOebgUQoH6EQLZcUFsIvxMZ+6kRVzf/MY/Bg+cMW+Jv3HRQUJ1mq3lGHxVmBOn5gEepwk2UjpcMjcaai6FOrQgWyrGq7wCyD85JxMnMNlzYQNxC+fw3J4hvjH5q6Kg9IsAy44BTBpgM76qHH"))
