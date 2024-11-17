import os

base = r'data/articles'


def clean_empty_files_and_folders(base_path):
    print("Starting cleanup process...")

    files_removed = 0
    folders_removed = 0

    for dirpath, dirnames, filenames in os.walk(base_path, topdown=False):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            try:
                if os.path.getsize(file_path) == 0:
                    print(f"Deleting empty file: {file_path}")
                    os.remove(file_path)
                    files_removed += 1
            except OSError as e:
                print(f"Error processing file {file_path}: {e}")

        # Then check if the directory is empty (after removing empty files)
        try:
            if not os.listdir(dirpath) and dirpath != base_path:
                print(f"Deleting empty folder: {dirpath}")
                os.rmdir(dirpath)
                folders_removed += 1
        except OSError as e:
            print(f"Error processing directory {dirpath}: {e}")

    print(f"- Empty files removed: {files_removed}")
    print(f"- Empty folders removed: {folders_removed}")


if os.path.exists(base):
    clean_empty_files_and_folders(base)
    print("\nCleanup process completed!")
else:
    print(f"Error: Base directory '{base}' does not exist!")
