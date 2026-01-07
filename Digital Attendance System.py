print("========== Digital Attendance System ==========")

attendance = {}   # Stores student name and attendance status

while True:
    print("\nChoose an option:")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. View Present Students")
    print("4. View Absent Students")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter student name: ").strip()
        status = input("Enter status (P for Present / A for Absent): ").upper()

        if status == "P":
            attendance[name] = "Present"
            print("Attendance marked as Present.")
        elif status == "A":
            attendance[name] = "Absent"
            print("Attendance marked as Absent.")
        else:
            print("Invalid status. Use P or A.")

    elif choice == "2":
        if not attendance:
            print("No attendance records available.")
        else:
            print("\n--- Attendance Record ---")
            for name, status in attendance.items():
                print(f"{name} : {status}")

    elif choice == "3":
        print("\n--- Present Students ---")
        found = False
        for name, status in attendance.items():
            if status == "Present":
                print(name)
                found = True
        if not found:
            print("No students marked Present.")

    elif choice == "4":
        print("\n--- Absent Students ---")
        found = False
        for name, status in attendance.items():
            if status == "Absent":
                print(name)
                found = True
        if not found:
            print("No students marked Absent.")

    elif choice == "5":
        print("Attendance system closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
