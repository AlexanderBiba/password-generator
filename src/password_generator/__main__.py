#!/usr/bin/env python

import argparse
import sys
from .password_generator import PasswordGenerator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=8, help="specify the length of the password")
    parser.add_argument("-d", "--digits", action="store_true", help="use digits")
    parser.add_argument("-c", "--chars", action="store_true", help="use alphanumeric ascii chars")
    # parser.add_argument("-c", "--clipboard", default=False, help="copy result to clipboard")
    args = parser.parse_args()

    if (args.digits is False and args.chars is False):
        print("One of -d/--digits or -c/--chars must be specified")
        sys.exit(1)

    password_generator = PasswordGenerator(args.length, args.digits, args.chars)
    password = password_generator.gen()
    print(password)