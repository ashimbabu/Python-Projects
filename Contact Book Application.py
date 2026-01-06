print("========== Contact Book Application ==========")

contacts = {}

while True:
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contacts[name] = {
                "phone": phone,
                "email": email
            }
            print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\n--- Contact List ---")
            for name, details in contacts.items():
                print(f"Name  : {name}")
                print(f"Phone : {details['phone']}")
                print(f"Email : {details['email']}")
                print("-------------------")

    elif choice == "3":
        name = input("Enter contact name to search: ")
        if name in contacts:
            print("\n--- Contact Found ---")
            print(f"Name  : {name}")
            print(f"Phone : {contacts[name]['phone']}")
            print(f"Email : {contacts[name]['email']}")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Contact Book closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
