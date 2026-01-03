print("----- Simple Quiz Game -----")

questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Pokhara", "B. Kathmandu", "C. Lalitpur", "D. Biratnagar"],
        "answer": "B"
    },
    {
        "question": "Which language is used to write Python?",
        "options": ["A. English", "B. Java", "C. C++", "D. Python"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit",
                    "C. Computer Personal Unit", "D. Central Power Unit"],
        "answer": "B"
    }
]

while True:
    print("\nMenu:")
    print("1. Start Quiz")
    print("2. Exit")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input! Enter 1 or 2.")
        continue

    if choice == 1:
        score = 0

        for q in questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)

            user_answer = input("Enter your answer (A/B/C/D): ").upper()

            if user_answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")

        print(f"\nQuiz completed! Your score: {score}/{len(questions)}")

    elif choice == 2:
        print("Quiz Game closed. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
