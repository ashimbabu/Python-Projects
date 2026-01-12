import os
import hashlib

def get_file_hash(file_path, block_size=65536):
    """Generate MD5 hash for a file"""
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None


def find_duplicates(folder_path):
    hash_dict = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)

            if file_hash:
                if file_hash in hash_dict:
                    hash_dict[file_hash].append(file_path)
                else:
                    hash_dict[file_hash] = [file_path]

    return hash_dict


print("===== Duplicate File Finder =====")
folder = input("Enter folder path to scan: ")

if not os.path.exists(folder):
    print("Folder does not exist!")
    exit()

duplicates = find_duplicates(folder)

found = False
for file_hash, files in duplicates.items():
    if len(files) > 1:
        found = True
        print("\nDuplicate files found:")
        for file in files:
            print(file)

if not found:
    print("\nNo duplicate files found.")
