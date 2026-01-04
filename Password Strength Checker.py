print("----- Password Strength Checker -----")

while True:
    print("\nMenu:")
    print("1. Check Password Strength")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        password = input("Enter your password: ")

        length = len(password)
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for ch in password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            else:
                has_symbol = True

        if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
            print("Password Strength: STRONG")
        elif length >= 6 and (has_upper or has_lower) and has_digit:
            print("Password Strength: MEDIUM")
        else:
            print("Password Strength: WEAK")

    elif choice == 2:
        print("Password Strength Checker closed.")
        break

    else:
        print("Invalid choice. Try again.")
