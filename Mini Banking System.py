print("----- Mini Banking System -----")

# Dictionary to store account details
accounts = {}

def create_account():
    account_number = input("Enter new account number: ").strip()
    if account_number in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder name: ").strip()
    accounts[account_number] = {"name": name, "balance": 0}
    print(f"Account created for {name} with account number {account_number}.")

def deposit():
    acc = input("Enter account number: ").strip()
    if acc not in accounts:
        print("Account not found!")
        return
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
        accounts[acc]["balance"] += amount
        print(f"Deposited {amount}. New balance: {accounts[acc]['balance']}")
    except ValueError:
        print("Invalid amount!")

def withdraw():
    acc = input("Enter account number: ").strip()
    if acc not in accounts:
        print("Account not found!")
        return
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
        if accounts[acc]["balance"] < amount:
            print("Insufficient balance!")
            return
        accounts[acc]["balance"] -= amount
        print(f"Withdrawn {amount}. New balance: {accounts[acc]['balance']}")
    except ValueError:
        print("Invalid amount!")

def check_balance():
    acc = input("Enter account number: ").strip()
    if acc not in accounts:
        print("Account not found!")
        return
    print(f"Account holder: {accounts[acc]['name']}")
    print(f"Balance: {accounts[acc]['balance']}")

# Main menu
while True:
    print("\nMenu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Banking system closed.")
        break
    else:
        print("Invalid choice. Try again.")
