# email_slicer.py

def slice_email(email):
    if "@" not in email:
        return None, None
    username, domain = email.split("@")
    return username, domain

def main():
    print("📧 Welcome to the Email Slicer!")
    email = input("Enter your email address: ")

    username, domain = slice_email(email)

    if username and domain:
        print(f"👤 Username: {username}")
        print(f"🌐 Domain: {domain}")
    else:
        print("❌ Invalid email address!")

if __name__ == "__main__":
    main()
