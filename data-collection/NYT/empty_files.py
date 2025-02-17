import os

base = r'data/NYT/articles'


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

                    str = file_path.replace("\\", "/")
                    parts = str.split('/')
                    print(parts)
                    topic = parts[3]
                    year = parts[4]
                    month = parts[5]
                    day = parts[6]
                    index = parts[7].split('.')[0]
                    month_number = month.split('month')[1]
                    day_number = day.split('day')[1]
                    source_path = f"data/NYT/source/{topic}/{year}/month{month_number}/{
                        year}_{month_number}_{day_number}_{index}.txt"
                    print(f"Deleting empty source: {source_path}")
                    os.remove(source_path)

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
