#!/usr/bin/env python

import argparse
import sys
import secrets
import string

class PasswordGenerator:
    def __init__(self, length=8, digits=False, chars=False, uppercase=False, lowercase=False, symbols=False, hexadecimal=False, octal=False, printable=False):
        self.length = length
        self.chars = chars
        self.digits = digits
        self.uppercase = uppercase
        self.lowercase = lowercase
        self.symbols = symbols
        self.hexadecimal = hexadecimal
        self.octal = octal
        self.printable = printable

    def gen(self):
        alphabet = ''
        if (self.chars): alphabet += string.ascii_letters
        if (self.digits): alphabet += string.digits
        if (self.uppercase): alphabet += string.uppercase
        if (self.lowercase): alphabet += string.lowercase
        if (self.symbols): alphabet += string.symbols
        if (self.hexadecimal): alphabet += string.hexadecimal
        if (self.octal): alphabet += string.octal
        if (self.printable): alphabet += string.printable
        return ''.join(secrets.choice(alphabet) for i in range(self.length))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--length", type=int, default=8, help="specify the length of the password")
    parser.add_argument("-d", "--digits", action="store_true", help="use digits")
    parser.add_argument("-c", "--chars", action="store_true", help="use alphanumeric ascii chars (uppercase and lowercase)")
    parser.add_argument("-u", "--uppercase", action="store_true", help="use uppercase ascii chars")
    parser.add_argument("-l", "--lowercase", action="store_true", help="use lowercase ascii chars")
    parser.add_argument("-s", "--symbols", action="store_true", help="use punctuation chars")
    parser.add_argument("-x", "--hex", action="store_true", help="use hexadecimal")
    parser.add_argument("-o", "--oct", action="store_true", help="use punctuation")
    parser.add_argument("-p", "--printable", action="store_true", help="use ascii chars considered printable")

    args = parser.parse_args()

    password_generator = PasswordGenerator(
        args.length,
        args.digits,
        args.chars,
        args.uppercase,
        args.lowercase
    )
    password = password_generator.gen()
    print(password)