print("----- Guess the Number -----")

while True:
    print("\nMenu:")
    print("1. Play Game")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if choice == 1:
        print("\nThink of a number between 1 and 100.")
        print("I will try to guess it.")
        print("Respond with: high, low, or correct")

        low = 1
        high = 100
        attempts = 0

        while True:
            if low > high:
                print("Something went wrong. Please check your answers.")
                break

            guess = (low + high) // 2
            attempts += 1
            print(f"\nMy guess is: {guess}")

            feedback = input("Is it high, low, or correct? ").lower()

            if feedback == "high":
                high = guess - 1
            elif feedback == "low":
                low = guess + 1
            elif feedback == "correct":
                print(f"I guessed your number in {attempts} attempts!")
                break
            else:
                print("Invalid response. Please type high, low, or correct.")

    elif choice == 2:
        print("Game closed. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
