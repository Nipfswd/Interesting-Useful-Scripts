from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

class Encryption:
    def __init__(self, passphrase):
        """Initialize AES encryption with a derived key."""
        salt = b'password_manager_salt'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = kdf.derive(passphrase.encode())

    def encrypt(self, plaintext):
        """Encrypt plaintext using AES."""
        iv = os.urandom(16)  # Generate random initialization vector
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        return iv + ciphertext  # Append IV to ciphertext

    def decrypt(self, ciphertext):
        """Decrypt ciphertext using AES."""
        iv = ciphertext[:16]  # Extract IV from ciphertext
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()
        return plaintext.decode()
