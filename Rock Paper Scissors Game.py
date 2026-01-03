import random

print("----- Rock Paper Scissors Game -----")

choices = ["rock", "paper", "scissors"]

while True:
    print("\nMenu:")
    print("1. Play Game")
    print("2. Exit")

    try:
        user_choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        continue

    if user_choice == 1:
        user_move = input("Choose rock, paper, or scissors: ").lower()

        if user_move not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_move = random.choice(choices)

        print(f"You chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        if user_move == computer_move:
            print("Result: It's a tie!")
        elif (
            (user_move == "rock" and computer_move == "scissors") or
            (user_move == "paper" and computer_move == "rock") or
            (user_move == "scissors" and computer_move == "paper")
        ):
            print("Result: You win!")
        else:
            print("Result: You lose!")

    elif user_choice == 2:
        print("Rock Paper Scissors Game closed.")
        break

    else:
        print("Invalid choice. Try again.")
