# Find Missing Files

This script identifies missing or empty directories for storing the articles in my folder structure. Here's how it works:

---

### **1. Iterates Through Data Structure**

The script loops through:

- **News sources**: e.g., _NYT_, _Guardian_.
- **Topics**: e.g., _politics_, _world_, _opinion_.
- **Years**: 2020 and 2021.
- **Months**: January to December.
- **Days**: 1 to 31.

---

### **2. Validates Dates**

- Ensures valid dates (e.g., skips invalid ones like February 30).

---

### **3. Checks Directories**

For each valid date, it:

- Constructs a directory path based on the current iteration.
- Checks if the directory exists.
- Verifies if the directory contains any files.

---

### **4. Tracks Missing/Empty Directories**

- If a directory is missing or empty, its path is recorded in a list.

---

### **5. Saves Results**

- Writes all missing or empty directory paths to a file named:  
  `missing_files.txt`.

This ensures any missing data is logged systematically for review. 😊
Thanks GPT for the inspiration!
