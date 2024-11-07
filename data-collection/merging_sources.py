import shutil
import os

# Define paths
aws_source_folder = r"C:\Users\L-Blu\Levi\Programmieren\Python\Jugend-Forscht\AWS\source"
data_source_folder = r"C:\Users\L-Blu\Levi\Programmieren\Python\Jugend-Forscht\data\source"

# Ensure destination folder exists
if not os.path.exists(data_source_folder):
    os.makedirs(data_source_folder)

# Copy files from AWS source to data source
for filename in os.listdir(aws_source_folder):
    aws_file_path = os.path.join(aws_source_folder, filename)
    if os.path.isfile(aws_file_path):
        shutil.copy(aws_file_path, data_source_folder)

print("Files copied successfully.")
