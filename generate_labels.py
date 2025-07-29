# This script generates a Labels.txt file for each class in the DAGM dataset (Class1 to Class6).
# It assigns a random label (0 = non-defective, 1 = defective) to each test image.

import os
import random

# Define the base directory where the DAGM dataset is stored
base_path = "./data"

# List of all class folders (Class1 to Class6)
classes = [f"Class{i}" for i in range(1, 7)]

# Loop through each class
for cls in classes:
    # Define where the test images are and where the label file should go
    image_dir = os.path.join(base_path, cls, "Test")
    label_dir = os.path.join(base_path, cls, "Label")
    label_file = os.path.join(label_dir, "Labels.txt")

    # Create the Label folder if it doesn't exist
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)

    # Get a sorted list of all test image files with .PNG extension
    image_files = [f for f in os.listdir(image_dir) if f.endswith(".PNG")]
    image_files.sort()

    # Create and write the Labels.txt file with headers and random labels
    with open(label_file, "w") as f:
        f.write("Index\tLabel\tFilename\n")  # Header line
        for idx, img in enumerate(image_files):
            label = random.choice([0, 1])  # Randomly choose between 0 or 1
            f.write(f"{idx}\t{label}\t{img}\n")  # Write each image entry

    # Print a confirmation message for this class
    print(f"✅ Labels.txt created for {cls} with {len(image_files)} entries")
