print("========== Electricity Bill Calculator ==========")

while True:
    print("\nChoose an option:")
    print("1. Calculate Electricity Bill")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        units = int(input("Enter total electricity units consumed: "))

        if units <= 20:
            bill = units * 4
        elif units <= 50:
            bill = (20 * 3) + ((units - 20) * 7.3)
        elif units <= 150:
            bill = (20 * 4) + (100 * 7.3) + ((units - 50) * 8.6)
        else:
            bill = (20 * 4) + (100 * 7.3) + (100 * 8.6) + ((units - 150) * 9.5)

        fixed_charge = 20
        total_bill = bill + fixed_charge

        print("\n--- Electricity Bill Details ---")
        print(f"Units Consumed : {units}")
        print(f"Energy Charge  : {bill}")
        print(f"Fixed Charge   : {fixed_charge}")
        print(f"Total Bill     : {total_bill}")

    elif choice == "2":
        print("Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
