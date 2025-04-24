import secrets
import string

class PasswordGenerator:
    def __init__(self, length=16, include_special=True):
        self.length = length
        self.include_special = include_special

    def generate(self):
        """Generate a secure random password."""
        characters = string.ascii_letters + string.digits
        if self.include_special:
            characters += "!@#$%^&*()-_=+<>?"
        return ''.join(secrets.choice(characters) for _ in range(self.length))
