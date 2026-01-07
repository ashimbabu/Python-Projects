print("========== Daily Expense Tracker ==========")

expenses = []

while True:
    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter expense category (Food, Travel, Bills, etc.): ")
        amount = float(input("Enter expense amount: "))

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\n--- Expense List ---")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. Date     : {exp['date']}")
                print(f"   Category : {exp['category']}")
                print(f"   Amount   : {exp['amount']}")
                print("---------------------")

    elif choice == "3":
        total = 0
        for exp in expenses:
            total += exp["amount"]
        print(f"\nTotal Expense: {total}")

    elif choice == "4":
        print("Expense Tracker closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
