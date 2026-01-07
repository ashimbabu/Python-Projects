print("===== Library Management System =====")

import os

# File to store book records
book_file = "books.txt"

# Ensure the file exists
if not os.path.exists(book_file):
    with open(book_file, "w") as f:
        pass

# Function to add book
def add_book():
    print("\n--- Add Book ---")
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    # Check for duplicate book ID
    with open(book_file, "r") as f:
        books = f.readlines()
        for book in books:
            if book_id == book.split(",")[0]:
                print("Book ID already exists!")
                return

    with open(book_file, "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")
    print("Book added successfully!")

# Function to view books
def view_books():
    print("\n--- Book List ---")
    with open(book_file, "r") as f:
        books = f.readlines()
        if not books:
            print("No books available.")
            return
        print("ID\tTitle\tAuthor\tStatus")
        for book in books:
            print("\t".join(book.strip().split(",")))

# Function to issue book
def issue_book():
    print("\n--- Issue Book ---")
    book_id = input("Enter Book ID to issue: ").strip()
    books_updated = []
    issued = False

    with open(book_file, "r") as f:
        books = f.readlines()
        for book in books:
            b_id, title, author, status = book.strip().split(",")
            if b_id == book_id:
                if status == "Available":
                    status = "Issued"
                    issued = True
                    print(f"Book '{title}' issued successfully!")
                else:
                    print(f"Book '{title}' is already issued.")
            books_updated.append(f"{b_id},{title},{author},{status}\n")

    with open(book_file, "w") as f:
        f.writelines(books_updated)

# Function to return book
def return_book():
    print("\n--- Return Book ---")
    book_id = input("Enter Book ID to return: ").strip()
    books_updated = []
    returned = False

    with open(book_file, "r") as f:
        books = f.readlines()
        for book in books:
            b_id, title, author, status = book.strip().split(",")
            if b_id == book_id:
                if status == "Issued":
                    status = "Available"
                    returned = True
                    print(f"Book '{title}' returned successfully!")
                else:
                    print(f"Book '{title}' is already available.")
            books_updated.append(f"{b_id},{title},{author},{status}\n")

    with open(book_file, "w") as f:
        f.writelines(books_updated)

# Main menu loop
while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Library System closed successfully.")
        break
    else:
        print("Invalid choice. Try again.")
