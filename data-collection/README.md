# Data Collection from the NYT

---

## New York Times Data Collection

#### Check out NYT Documentation [here](./NYT/)

---

## Guardian Data Collection

#### Check out NYT Documentation [here](./Guardian/)

---

## Step 2.5: Optimize Data Collection

##### 1. Use AWS to run Python in the cloud

- See my Subfolder [AWS - How to Run Python in the Cloud](./AWS/)

- Run your scripts in the Cloud to reduce computer usage

##### 2. Use Multiprocessing to run Multiple Threads at once

- See my Subfolder and Documentation at [Multiprocessing](./Multiprocessing/)

---

## 3. Extra Functionality

1. **Find empty files**:

   - Sometimes the content wasnt downloaded correcly so i checked where there where empty files without content.

     ```python
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
     ```

   - Again, this depends on your folder structure.

2. **Find missing files**:

   - To check what files are missing i used a simple script
   - Thanks Copilot 😃
   - See `file_checker.py`

---

## Result

- This is only a part of the full project!

- The part, where we extract the full NYT Article Text

- View the whole Projekt at [Github](https://github.com/AdminL3/Jugend-Forscht/)
