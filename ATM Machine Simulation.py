print("========== ATM Machine Simulation ==========")

balance = 10000  # Initial balance

while True:
    print("\nChoose an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: {balance}")

    elif choice == "2":
        deposit = float(input("Enter amount to deposit: "))
        if deposit > 0:
            balance += deposit
            print(f"Amount deposited successfully. New balance: {balance}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= 0:
            print("Invalid withdrawal amount.")
        elif withdraw > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw
            print(f"Please collect your cash.")
            print(f"Remaining balance: {balance}")

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
