import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog

# Function to arrange files in a directory
def arrange_files(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Create a dictionary to store file extensions and their corresponding folders
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".doc", ".docx", ".txt", ".pdf"],
        "Videos": [".mp4", ".avi", ".mov"],
        "Music": [".mp3", ".wav"],
        "Others": []  # Files with unknown extensions
    }

    # Create folders for each file extension, if they don't exist
    for folder in extensions:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to their respective folders
    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            file_extension = os.path.splitext(file)[1].lower()
            moved = False
            for folder, ext_list in extensions.items():
                if file_extension in ext_list:
                    src_path = os.path.join(directory, file)
                    dest_path = os.path.join(directory, folder, file)
                    shutil.move(src_path, dest_path)
                    moved = True
                    break
            if not moved:
                src_path = os.path.join(directory, file)
                dest_path = os.path.join(directory, "Others", file)
                shutil.move(src_path, dest_path)

    print("File arranging completed.")

# Function to handle the directory selection
def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        arrange_files(directory)
        open_directory(directory)

# Function to open the arranged directory in the file explorer (Windows only)
def open_directory(directory):
    if os.name == 'nt':
        subprocess.run(["explorer", directory])

# Create the main Tkinter window
window = tk.Tk()
window.title("File Arranger")

# Create the directory selection button
select_button = tk.Button(window, text="Select Directory", command=select_directory)
select_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
