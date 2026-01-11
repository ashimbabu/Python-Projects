import time
import random

sentences = [
    "Python is a powerful programming language",
    "Typing speed improves with regular practice",
    "Machine learning is part of artificial intelligence",
    "Geographic information systems handle spatial data",
    "Practice makes a programmer perfect"
]

print("===== Typing Speed Test =====")
print("You will be given a sentence to type.")
print("Type it exactly as shown and press Enter.\n")

sentence = random.choice(sentences)
print("Sentence:")
print(sentence)
print()

input("Press Enter when you are ready to start...")

start_time = time.time()
typed_text = input("\nStart typing:\n")
end_time = time.time()

time_taken = end_time - start_time

# Calculate words per minute
word_count = len(sentence.split())
wpm = (word_count / time_taken) * 60

# Calculate accuracy
correct_chars = 0
for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

print("\n===== Result =====")
print(f"Time Taken: {round(time_taken, 2)} seconds")
print(f"Typing Speed: {round(wpm, 2)} WPM")
print(f"Accuracy: {round(accuracy, 2)} %")
