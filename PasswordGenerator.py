import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_specials):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 🎯 User interaction
print("Welcome to PASSWORD GENERATOR\n")

try:
    length = int(input("Enter desired password length: "))
    
    print("\nSelect character types to include:")
    use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (e.g., @, #, $) (y/n): ").lower() == 'y'
    password = generate_password(length, use_upper, use_lower, use_digits, use_specials)
    print("\nYour Generated Password:",password)

except ValueError:
    print("❌ Please enter a valid number for length.")