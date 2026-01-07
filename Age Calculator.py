print("========== Age Calculator ==========")

while True:
    print("\nChoose an option:")
    print("1. Calculate Age")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        birth_year = int(input("Enter your birth year (YYYY): "))
        current_year = int(input("Enter current year (YYYY): "))

        if birth_year > current_year:
            print("Invalid input! Birth year cannot be greater than current year.")
        else:
            age = current_year - birth_year
            print(f"\nYour Age is: {age} years")

    elif choice == "2":
        print("Age Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
