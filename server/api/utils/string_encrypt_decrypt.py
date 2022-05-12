import rsa

class StringEncrypterDecrypter:

    def __init__(self, publicKey, privateKey) -> None:
        self.publicKey, self.privateKey = rsa.newKeys(512)

    def encrypt_string(self, plain_text): 
        return rsa.encrypt(plain_text.encode(),
                         self.publicKey)

    def decrypt_string(self, encrypted_string):
        return rsa.decrypt(encrypted_string, self.privateKey).decode()
