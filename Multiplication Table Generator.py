print("========== Multiplication Table Generator ==========")

while True:
    print("\nChoose an option:")
    print("1. Generate Multiplication Table")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        number = int(input("Enter a number: "))
        limit = int(input("Enter the limit: "))

        print(f"\nMultiplication Table of {number}:\n")

        for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")

    elif choice == "2":
        print("Multiplication Table Generator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
