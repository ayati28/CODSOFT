import random
import string

print("🔐 Password Generator")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:", password)

strength = "Weak"

if length >= 12:
    strength = "Strong"
elif length >= 8:
    strength = "Medium"

print("Password Strength:", strength)