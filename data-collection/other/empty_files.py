import os


base = r'C:\Users\L-Blu\Levi\Programmieren\Python\Jugend-Forscht\data\articles'
base2 = 'C:\\Users\\L-Blu\\Levi\\Programmieren\\Python\\Jugend-Forscht\\data\\source\\'


for _ in range(2):
    for dirpath, dirnames, filenames in os.walk(base, topdown=False):
        # Check if the directory is empty
        if not os.listdir(dirpath):  # If the folder is empty
            print(f"Deleting empty folder: {dirpath}")
            os.rmdir(dirpath)  # Delete the empty folder

        # Also check for empty files and delete them
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.getsize(file_path) == 0:  # If the file is empty
                print(f"Deleting empty file: {file_path}")
                os.remove(file_path)
                os.remove(os.path.join(
                    base2 + os.path.join('\\'.join(file_path.split('\\')[9:14]))))
