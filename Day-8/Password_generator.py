# password_generator.py

import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Must be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"💡 Generated Password: {password}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()
