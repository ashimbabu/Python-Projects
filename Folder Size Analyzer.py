import os

print("===== Folder Size Analyzer =====")

folder_path = input("Enter folder path: ")

total_size = 0
file_count = 0
folder_count = 0
largest_file = ""
largest_size = 0

try:
    for root, dirs, files in os.walk(folder_path):
        folder_count += len(dirs)

        for file in files:
            file_count += 1
            file_path = os.path.join(root, file)

            try:
                size = os.path.getsize(file_path)
                total_size += size

                if size > largest_size:
                    largest_size = size
                    largest_file = file_path
            except:
                pass

    print("\nFolder Analysis Report")
    print("----------------------")
    print("Total folders :", folder_count)
    print("Total files   :", file_count)
    print("Total size    :", round(total_size / (1024 * 1024), 2), "MB")

    if largest_file:
        print("\nLargest File:")
        print(largest_file)
        print("Size:", round(largest_size / (1024 * 1024), 2), "MB")

except FileNotFoundError:
    print("Invalid folder path. Please try again.")
