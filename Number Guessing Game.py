import random

print("🎯 Welcome to the Number Guessing Game! 🎯")

while True:
    print("\nMenu:")
    print("1. Play Game")
    print("2. Exit")
    
    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Enter 1 or 2.")
        continue
    
    if choice == 1:
        # Computer picks a random number between 1 and 100
        number = random.randint(1, 100)
        attempts = 0
        print("\nI have selected a number between 1 and 100. Can you guess it?")
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
                break

    elif choice == 2:
        print("Exiting Number Guessing Game. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")
