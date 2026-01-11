print("===== File-Based Word Counter =====")

file_name = input("Enter file name (with .txt): ")

try:
    with open(file_name, "r") as file:
        text = file.read()

        # Count characters
        char_count = len(text)

        # Count words
        word_count = len(text.split())

        # Count lines
        line_count = text.count("\n") + 1

    print("\nResults:")
    print("Characters:", char_count)
    print("Words:", word_count)
    print("Lines:", line_count)

except FileNotFoundError:
    print("File not found! Please check the file name.")