# Import the os module to handle directory operations
import os

# Define the root directory where the class folders are stored
data_root = "./data"

# Loop through Class1 to Class6 and check subdirectories inside Train and Test folders
for i in range(1, 7):
    for split in ["Train", "Test"]:
        path = os.path.join(data_root, f"Class{i}", split)
        if os.path.exists(path):
            subdirs = os.listdir(path)
            print(f"{path} → {subdirs}")  # Print the contents of each Train/Test folder
