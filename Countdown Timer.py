import time

print("----- Countdown Timer -----")

while True:
    print("\nMenu:")
    print("1. Start Timer")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        try:
            seconds = int(input("Enter time in seconds: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if seconds <= 0:
            print("Time must be greater than zero.")
            continue

        print("\nTimer started...")
        while seconds > 0:
            mins = seconds // 60
            secs = seconds % 60
            print(f"Time left: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1

        print("⏰ Time's up!")

    elif choice == 2:
        print("Countdown Timer closed.")
        break

    else:
        print("Invalid choice. Try again.")
