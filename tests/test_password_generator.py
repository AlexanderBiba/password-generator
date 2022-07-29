from password_generator.password_generator import PasswordGenerator
import string
import pytest

def test_zero():
    password = PasswordGenerator(0).gen()
    assert len(password) == 0

def test_no_alphabet():
    with pytest.raises(IndexError):
        password = PasswordGenerator(1).gen()

def test_digits():
    passwordLength = 14
    password = PasswordGenerator(14, digits=True).gen()
    assert len(password) == passwordLength
    assert all(c in string.digits for c in password)

def test_chars():
    passwordLength = 12
    password = PasswordGenerator(passwordLength, chars=True).gen()
    assert len(password) == passwordLength
    assert all(c in string.ascii_letters for c in password)