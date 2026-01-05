print("========== Compound Interest Calculator ==========")

while True:
    print("\nChoose an option:")
    print("1. Calculate Compound Interest")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (%): "))
        time = float(input("Enter Time (in years): "))
        n = int(input("Enter number of times interest is compounded per year: "))

        amount = principal * (1 + rate / (100 * n)) ** (n * time)
        compound_interest = amount - principal

        print("\n--- Result ---")
        print(f"Compound Interest : {compound_interest:.2f}")
        print(f"Total Amount      : {amount:.2f}")

    elif choice == "2":
        print("Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
