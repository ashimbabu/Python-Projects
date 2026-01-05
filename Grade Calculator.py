print("========== Grade Calculator ==========")

while True:
    print("\nChoose an option:")
    print("1. Calculate Grade")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        total_subjects = int(input("Enter number of subjects: "))
        total_marks = 0

        for i in range(1, total_subjects + 1):
            marks = int(input(f"Enter marks for subject {i}: "))
            total_marks += marks

        percentage = total_marks / total_subjects

        print("\n--- Result ---")
        print(f"Total Marks : {total_marks}")
        print(f"Percentage  : {percentage:.2f}%")

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B+"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "Fail"

        print(f"Grade       : {grade}")

    elif choice == "2":
        print("Calculator closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
