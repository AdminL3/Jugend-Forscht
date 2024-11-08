import shutil
import os

# Define paths
aws_source_folder = r"C:\Users\L-Blu\Levi\Programmieren\Python\Jugend-Forscht\AWS\source"
data_source_folder = r"C:\Users\L-Blu\Levi\Programmieren\Python\Jugend-Forscht\data\source"

# Ensure destination folder exists
if not os.path.exists(data_source_folder):
    os.makedirs(data_source_folder)

# Function to copy files and folders recursively


def copy_files_and_folders(aws_folder, data_folder):
    # Check all items in the current folder
    for item in os.listdir(aws_folder):
        aws_item_path = os.path.join(aws_folder, item)
        data_item_path = os.path.join(data_folder, item)

        if os.path.isdir(aws_item_path):
            # Handle directories: Check if it exists, if not, create it
            if not os.path.exists(data_item_path):
                os.makedirs(data_item_path)
                print(f"New folder created: {item}")
            else:
                print(f"Folder already exists: {item}", end='  ')

            # Recursively call the function to handle files in this subfolder
            copy_files_and_folders(aws_item_path, data_item_path)

        elif os.path.isfile(aws_item_path):
            # Handle files: Check if the file exists
            if not os.path.exists(data_item_path):
                shutil.copy(aws_item_path, data_item_path)
                print(f"New file added: {item} \n\n")
            else:
                print(f"File already exists: {item}", end='  ')


# Start the copying process
copy_files_and_folders(aws_source_folder, data_source_folder)

print("File and folder copy process completed.")
