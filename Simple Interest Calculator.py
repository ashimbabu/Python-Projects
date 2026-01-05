print("----- Simple Interest Calculator -----")

while True:
    print("\nChoose an option:")
    print("1. Calculate Simple Interest")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (%): "))
        time = float(input("Enter Time (in years): "))

        simple_interest = (principal * rate * time) / 100
        total_amount = principal + simple_interest

        print(f"Simple Interest = {simple_interest}")
        print(f"Total Amount = {total_amount}")

    elif choice == "2":
        print("Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
