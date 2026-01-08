import hashlib
import os

print("===== Secure Login System =====")

USER_FILE = "users.txt"

# Create file if not exists
if not os.path.exists(USER_FILE):
    open(USER_FILE, "w").close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    print("\n--- Register ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    with open(USER_FILE, "r") as f:
        for line in f:
            if username == line.split(",")[0]:
                print("Username already exists!")
                return

    hashed_pwd = hash_password(password)

    with open(USER_FILE, "a") as f:
        f.write(f"{username},{hashed_pwd}\n")

    print("Registration successful!")

def login():
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    hashed_pwd = hash_password(password)

    attempts = 3

    while attempts > 0:
        with open(USER_FILE, "r") as f:
            for line in f:
                stored_user, stored_pwd = line.strip().split(",")
                if username == stored_user and hashed_pwd == stored_pwd:
                    print(f"Login successful! Welcome, {username}")
                    return

        attempts -= 1
        print(f"Invalid credentials! Attempts left: {attempts}")
        if attempts > 0:
            password = input("Re-enter password: ").strip()
            hashed_pwd = hash_password(password)

    print("Account locked! Too many failed attempts.")

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("System exited securely.")
        break
    else:
        print("Invalid option. Try again.")
