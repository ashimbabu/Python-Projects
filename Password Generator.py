import random
import string

print("----- Password Generator -----")

while True:
    print("\n1. Generate Password")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        try:
            length = int(input("Enter password length: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if length <= 0:
            print("Password length must be greater than 0.")
            continue

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    elif choice == 2:
        print("Password Generator closed.")
        break

    else:
        print("Invalid choice. Try again.")
