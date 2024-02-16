# 8. Password Guesser:
# Design a simple program that generates random passwords from a set of characters 
# (lowercase, uppercase, numbers, symbols). The password length and character limitations can 
# be stored in a dictionary.
import random
import string

def gen_pas(length, include_uppercase=True, include_lowercase=True, include_numbers=True, include_symbols=True):
    chr = ''
    if include_lowercase:
        chr += string.ascii_lowercase
    if include_uppercase:
        chr += string.ascii_uppercase
    if include_numbers:
        chr += string.digits
    if include_symbols:
        chr += string.punctuation
    return ''.join(random.choice(chr) for _ in range(length))
#dictionary 
dic = {}
password_length = 10
a = gen_pas(password_length)
dic[password_length] = a
print(a)
print(dic)