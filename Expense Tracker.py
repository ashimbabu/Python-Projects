import csv
import os
from datetime import datetime

print("===== Expense Tracker =====")

FILE_NAME = "expenses.csv"

# Create CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Category (Food, Travel, Rent, etc.): ")
    amount = float(input("Amount: "))
    description = input("Description: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")

def view_summary():
    total = 0
    category_total = {}

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row["Amount"])
            total += amount
            category_total[row["Category"]] = category_total.get(row["Category"], 0) + amount

    print("\n--- Expense Summary ---")
    print(f"Total Expense: {total}")
    for cat, amt in category_total.items():
        print(f"{cat}: {amt}")

def monthly_report():
    month = input("Enter month (YYYY-MM): ")
    total = 0

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print(f"Total expense for {month}: {total}")

while True:
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Monthly Report")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        monthly_report()
    elif choice == "4":
        print("Expense Tracker closed.")
        break
    else:
        print("Invalid choice.")
