import os
import string

print("===== Mini Search Engine =====")

DOC_FOLDER = "documents"

def load_documents():
    documents = {}
    for file in os.listdir(DOC_FOLDER):
        if file.endswith(".txt"):
            with open(os.path.join(DOC_FOLDER, file), "r", encoding="utf-8") as f:
                text = f.read().lower()
                text = text.translate(str.maketrans("", "", string.punctuation))
                documents[file] = text
    return documents

def build_index(documents):
    index = {}
    for doc, text in documents.items():
        words = text.split()
        for word in words:
            index[word] = index.get(word, {})
            index[word][doc] = index[word].get(doc, 0) + 1
    return index

def search(query, index):
    results = {}
    query_words = query.lower().split()

    for word in query_words:
        if word in index:
            for doc, count in index[word].items():
                results[doc] = results.get(doc, 0) + count

    return sorted(results.items(), key=lambda x: x[1], reverse=True)

def main():
    documents = load_documents()
    index = build_index(documents)

    while True:
        print("\nMenu:")
        print("1. Search")
        print("2. Exit")

        choice = input("Enter choice (1-2): ")

        if choice == "1":
            query = input("Enter search query: ")
            results = search(query, index)

            if results:
                print("\nSearch Results (Ranked):")
                for doc, score in results:
                    print(f"{doc} → relevance score: {score}")
            else:
                print("No matching documents found.")

        elif choice == "2":
            print("Search Engine closed.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
