import os

FILE_NAME = "users.txt"

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_user, _ = line.strip().split(",")
                if stored_user == username:
                    print("Username already exists!")
                    return

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not os.path.exists(FILE_NAME):
        print("No users registered yet!")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")
            if stored_user == username and stored_pass == password:
                print("Login successful!")
                return

    print("Invalid username or password!")


while True:
    print("\n===== Login & Registration System =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Program closed")
        break
    else:
        print("Invalid choice!")
