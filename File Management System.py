import os
import shutil

print("===== File Management System =====")

def list_items(path):
    try:
        items = os.listdir(path)
        if not items:
            print("Directory is empty.")
        else:
            for item in items:
                print(item)
    except FileNotFoundError:
        print("Invalid path!")

def create_file(path):
    filename = input("Enter file name: ")
    full_path = os.path.join(path, filename)
    open(full_path, "w").close()
    print("File created successfully.")

def create_folder(path):
    folder_name = input("Enter folder name: ")
    os.makedirs(os.path.join(path, folder_name), exist_ok=True)
    print("Folder created successfully.")

def delete_item(path):
    name = input("Enter file/folder name to delete: ")
    full_path = os.path.join(path, name)
    if os.path.isfile(full_path):
        os.remove(full_path)
        print("File deleted.")
    elif os.path.isdir(full_path):
        shutil.rmtree(full_path)
        print("Folder deleted.")
    else:
        print("Item not found.")

def rename_item(path):
    old_name = input("Enter current name: ")
    new_name = input("Enter new name: ")
    os.rename(os.path.join(path, old_name), os.path.join(path, new_name))
    print("Renamed successfully.")

def copy_file(path):
    file_name = input("Enter file name to copy: ")
    destination = input("Enter destination path: ")
    shutil.copy(os.path.join(path, file_name), destination)
    print("File copied successfully.")

def move_file(path):
    file_name = input("Enter file name to move: ")
    destination = input("Enter destination path: ")
    shutil.move(os.path.join(path, file_name), destination)
    print("File moved successfully.")

def organize_by_extension(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            ext = file.split(".")[-1]
            folder = os.path.join(path, ext.upper())
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(path, file), folder)
    print("Files organized by extension.")

while True:
    print("\nMenu:")
    print("1. View Files/Folders")
    print("2. Create File")
    print("3. Create Folder")
    print("4. Delete File/Folder")
    print("5. Rename File/Folder")
    print("6. Copy File")
    print("7. Move File")
    print("8. Organize Files by Extension")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")
    path = input("Enter directory path: ")

    if choice == "1":
        list_items(path)
    elif choice == "2":
        create_file(path)
    elif choice == "3":
        create_folder(path)
    elif choice == "4":
        delete_item(path)
    elif choice == "5":
        rename_item(path)
    elif choice == "6":
        copy_file(path)
    elif choice == "7":
        move_file(path)
    elif choice == "8":
        organize_by_extension(path)
    elif choice == "9":
        print("File Management System closed.")
        break
    else:
        print("Invalid choice.")
