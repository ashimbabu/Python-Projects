import os

print("----- Bulk File Renamer -----")

while True:
    print("\nMenu:")
    print("1. Rename Files")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        folder = input("Enter the folder path: ")
        if not os.path.exists(folder):
            print("Folder does not exist. Please check the path.")
            continue

        os.chdir(folder)
        print(f"Files in folder: {os.listdir()}")

        prefix = input("Enter prefix to add (press enter to skip): ")
        suffix = input("Enter suffix to add (press enter to skip): ")

        for filename in os.listdir():
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name}{suffix}{ext}"
            os.rename(filename, new_name)

        print("Files renamed successfully!")
        print(f"Updated files: {os.listdir()}")

    elif choice == 2:
        print("Bulk File Renamer closed.")
        break

    else:
        print("Invalid choice. Try again.")
