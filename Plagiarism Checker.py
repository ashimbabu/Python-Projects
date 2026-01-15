print("===== Plagiarism Checker =====")

def read_file(filename):
    with open(filename, "r") as file:
        return file.read().lower()

def calculate_similarity(text1, text2):
    words1 = set(text1.split())
    words2 = set(text2.split())

    common_words = words1.intersection(words2)
    total_words = words1.union(words2)

    similarity = (len(common_words) / len(total_words)) * 100
    return similarity

try:
    file1 = input("Enter first file name (example: file1.txt): ")
    file2 = input("Enter second file name (example: file2.txt): ")

    text1 = read_file(file1)
    text2 = read_file(file2)

    similarity_percentage = calculate_similarity(text1, text2)

    print("\n===== Plagiarism Report =====")
    print(f"Similarity Percentage: {similarity_percentage:.2f}%")

    if similarity_percentage > 70:
        print("Plagiarism Level: HIGH ❌")
    elif similarity_percentage > 40:
        print("Plagiarism Level: MEDIUM ⚠️")
    else:
        print("Plagiarism Level: LOW ✅")

except FileNotFoundError:
    print("Error: One or both files not found.")