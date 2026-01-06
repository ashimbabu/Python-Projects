print("========== Smart Study Planner ==========")

study_plan = []

while True:
    print("\nChoose an option:")
    print("1. Add Study Task")
    print("2. View Study Plan")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        subject = input("Enter subject name: ")
        topic = input("Enter topic to study: ")
        hours = input("Enter study hours: ")

        task = {
            "subject": subject,
            "topic": topic,
            "hours": hours,
            "status": "Pending"
        }

        study_plan.append(task)
        print("Study task added successfully!")

    elif choice == "2":
        if not study_plan:
            print("No study tasks available.")
        else:
            print("\n--- Study Plan ---")
            for index, task in enumerate(study_plan, start=1):
                print(f"{index}. Subject : {task['subject']}")
                print(f"   Topic   : {task['topic']}")
                print(f"   Hours   : {task['hours']}")
                print(f"   Status  : {task['status']}")
                print("-----------------------")

    elif choice == "3":
        task_no = int(input("Enter task number to mark completed: "))
        if 1 <= task_no <= len(study_plan):
            study_plan[task_no - 1]["status"] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(study_plan):
            removed_task = study_plan.pop(task_no - 1)
            print(f"Task '{removed_task['topic']}' deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Study Planner closed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
