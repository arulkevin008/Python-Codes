import random
import string

def generate_password():
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special_chars else ''
    all_chars = lower + upper + digits + special
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special_chars:
        password.append(random.choice(special))
    password.append(random.choice(lower))
    while len(password) < length:
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return'' .join(password)
print("Generated Password:", generate_password())
