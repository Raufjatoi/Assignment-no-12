# 8. Password Guesser:
# Design a simple program that generates random passwords from a set of characters 
# (lowercase, uppercase, numbers, symbols). The password length and character limitations can 
# be stored in a dictionary.
import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_numbers=True, include_symbols=True):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# Example usage
password_length = 12
password = generate_password(password_length)
print("Generated Password:", password)
