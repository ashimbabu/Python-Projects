print("===== Duplicate Sentence Detector =====")

try:
    filename = input("Enter text file name (example: notes.txt): ")

    with open(filename, "r") as file:
        text = file.read().lower()

    # Split text into sentences
    sentences = text.replace("\n", " ").split(".")

    sentence_count = {}
    duplicates = {}

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 5:  # ignore very short sentences
            if sentence in sentence_count:
                sentence_count[sentence] += 1
                duplicates[sentence] = sentence_count[sentence]
            else:
                sentence_count[sentence] = 1

    print("\n===== Duplicate Sentence Report =====")

    if duplicates:
        for sentence, count in duplicates.items():
            print(f"'{sentence}' → repeated {count} times")
    else:
        print("No duplicate sentences found.")

except FileNotFoundError:
    print("Error: File not found. Please check file name.")
