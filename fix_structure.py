import os
import shutil

# Define the root directory where all the Class folders are located
root_dir = "data"

# Loop through Class1 to Class6
for i in range(1, 7):
    # Construct the path to the inner nested folder (e.g., data/Class1/Class1)
    inner_path = os.path.join(root_dir, f"Class{i}", f"Class{i}")
    
    # Construct the path to the outer Class folder (e.g., data/Class1)
    outer_path = os.path.join(root_dir, f"Class{i}")

    # Check if the nested folder exists (sometimes DAGM dataset has this issue)
    if os.path.exists(inner_path):
        print(f"Fixing Class{i}...")

        # Move all files from the inner folder to the outer Class folder
        for item in os.listdir(inner_path):
            src = os.path.join(inner_path, item)
            dst = os.path.join(outer_path, item)
            shutil.move(src, dst)

        # Delete the now-empty inner folder
        os.rmdir(inner_path)
    else:
        print(f"No nested folder for Class{i}")
