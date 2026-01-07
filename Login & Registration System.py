print("===== Login & Registration System =====")

import os

# File to store user credentials
file_name = "users.txt"

# Ensure the file exists
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        pass

def register():
    print("\n--- Register ---")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()

    # Check if username already exists
    with open(file_name, "r") as f:
        users = f.readlines()
        for user in users:
            existing_username = user.split(",")[0]
            if username == existing_username:
                print("Username already exists! Try a different one.")
                return

    # Store new user
    with open(file_name, "a") as f:
        f.write(f"{username},{password}\n")
    print("Registration successful!")

def login():
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    with open(file_name, "r") as f:
        users = f.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(",")
            if username == stored_username and password == stored_password:
                print(f"Login successful! Welcome, {username}.")
                return
        print("Invalid username or password!")

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
        print("System closed successfully.")
        break
    else:
        print("Invalid choice! Try again.")
