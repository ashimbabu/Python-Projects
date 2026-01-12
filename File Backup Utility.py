import os
import shutil
from datetime import datetime

print("===== File Backup Utility =====")

# Input source and backup folders
source_folder = input("Enter source folder path: ")
backup_root = input("Enter backup folder path: ")

# Check if source folder exists
if not os.path.exists(source_folder):
    print("Source folder does not exist!")
    exit()

# Create a timestamped backup folder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(backup_root, "Backup_" + timestamp)

os.makedirs(backup_folder)
print(f"Backup folder created: {backup_folder}")

# Copy files
for item in os.listdir(source_folder):
    source_item = os.path.join(source_folder, item)
    dest_item = os.path.join(backup_folder, item)

    if os.path.isfile(source_item):
        shutil.copy2(source_item, dest_item)
        print(f"Copied file: {item}")
    elif os.path.isdir(source_item):
        shutil.copytree(source_item, dest_item)
        print(f"Copied folder: {item}")

print("\nBackup completed successfully!")
