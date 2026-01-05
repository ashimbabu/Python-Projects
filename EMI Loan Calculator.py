print("========== EMI Loan Calculator ==========")

while True:
    print("\nChoose an option:")
    print("1. Calculate EMI")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        loan_amount = float(input("Enter Loan Amount: "))
        annual_rate = float(input("Enter Annual Interest Rate (%): "))
        tenure_years = int(input("Enter Loan Tenure (in years): "))

        monthly_rate = annual_rate / (12 * 100)
        total_months = tenure_years * 12

        emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** total_months) / \
              ((1 + monthly_rate) ** total_months - 1)

        total_payment = emi * total_months
        total_interest = total_payment - loan_amount

        print("\n--- EMI Details ---")
        print(f"Monthly EMI        : {emi:.2f}")
        print(f"Total Payment      : {total_payment:.2f}")
        print(f"Total Interest     : {total_interest:.2f}")

    elif choice == "2":
        print("Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
