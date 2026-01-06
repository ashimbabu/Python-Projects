print("========== Bank Management System ==========")

accounts = {}   # Dictionary to store account details

while True:
    print("\nChoose an option:")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            print("Account already exists!")
        else:
            name = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: "))
            accounts[acc_no] = {
                "name": name,
                "balance": balance
            }
            print("Account created successfully!")

    elif choice == "2":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            print("\n--- Account Details ---")
            print(f"Account Number : {acc_no}")
            print(f"Name           : {accounts[acc_no]['name']}")
            print(f"Balance        : {accounts[acc_no]['balance']}")
        else:
            print("Account not found!")

    elif choice == "3":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                accounts[acc_no]["balance"] += amount
                print("Deposit successful!")
                print(f"New Balance: {accounts[acc_no]['balance']}")
            else:
                print("Invalid amount.")
        else:
            print("Account not found!")

    elif choice == "4":
        acc_no = input("Enter Account Number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount.")
            elif amount > accounts[acc_no]["balance"]:
                print("Insufficient balance!")
            else:
                accounts[acc_no]["balance"] -= amount
                print("Withdrawal successful!")
                print(f"Remaining Balance: {accounts[acc_no]['balance']}")
        else:
            print("Account not found!")

    elif choice == "5":
        print("System exited successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
