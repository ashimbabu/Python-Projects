task_lists = []

while True:

    print("Welcome to the To-Do List App!")
    print("\n1. Add Tasks \n2. View Tasks \n3. Remove Tasks \n4. Exit")

    user_choice = int(input("Please enter your choice:"))
    if user_choice == 1:
        task = input("Enter your task: ")
        task_lists.append(task)
        print("Task added successfully!")

    elif user_choice == 2:
        print(task_lists)

    elif user_choice == 3:
        task = input("Enter tasks to remove:")
        task_lists.remove(task)
        print("Task removed successfully!")

    elif user_choice == 4:
        print("Bye")
        break

    else:
        print("Invalid choice.")