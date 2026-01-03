print("----- Mad Libs Game -----")

while True:
    print("\n1. Play Mad Libs")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        name = input("Enter a name: ")
        place = input("Enter a place: ")
        animal = input("Enter an animal: ")
        adjective = input("Enter an adjective: ")
        verb = input("Enter a verb: ")

        story = f"""
Once upon a time, {name} went to {place}.
There, {name} saw a very {adjective} {animal}.
The {animal} started to {verb}, and everyone was surprised!
"""

        print("\n--- Your Mad Libs Story ---")
        print(story)

    elif choice == 2:
        print("Mad Libs Game closed. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
