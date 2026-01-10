print("===== Word Counter =====")

text = input("Enter a sentence or paragraph: ")

# Count characters (including spaces)
char_count = len(text)

# Count words
words = text.split()
word_count = len(words)

# Count sentences
sentence_count = 0
for ch in text:
    if ch in ".!?":
        sentence_count += 1

print("\nResults:")
print("Characters:", char_count)
print("Words:", word_count)
print("Sentences:", sentence_count)
