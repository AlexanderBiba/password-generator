import secrets
import string

class PasswordGenerator:
    def __init__(self, length=8, digits=False, chars=False):
        self.length = length
        self.chars = chars
        self.digits = digits

    def gen(self):
        alphabet = ''
        if (self.chars): alphabet += string.ascii_letters
        if (self.digits): alphabet += string.digits
        return ''.join(secrets.choice(alphabet) for i in range(self.length))
