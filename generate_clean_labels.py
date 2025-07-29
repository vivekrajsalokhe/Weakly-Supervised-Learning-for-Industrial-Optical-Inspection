# save this as generate_clean_labels.py
# This script generates a text file (clean_labels.txt) listing the relative path and label of each image 
# from all Class folders (Class1 to Class6) that have been organized into Train/Test/0 and Train/Test/1.

import os

# Set the root folder where your Class1 to Class6 folders are located
data_root = "./data"

# Define the name of the output label file
output_file = "clean_labels.txt"

# Open the output file in write mode
with open(output_file, "w") as f:
    # Loop through each class folder (e.g., Class1, Class2, ...)
    for class_name in sorted(os.listdir(data_root)):
        class_path = os.path.join(data_root, class_name)
        
        # Skip anything that is not a directory
        if not os.path.isdir(class_path):
            continue
        
        # Loop through both Train and Test folders
        for split in ["Train", "Test"]:
            split_path = os.path.join(class_path, split)
            
            # Skip if the Train or Test folder doesn't exist
            if not os.path.isdir(split_path):
                continue
            
            # Loop through both class labels: 0 = non-defective, 1 = defective
            for label in ["0", "1"]:
                label_path = os.path.join(split_path, label)
                
                # Skip if the label folder doesn't exist
                if not os.path.isdir(label_path):
                    continue
                
                # Loop through each image file in the label folder
                for fname in os.listdir(label_path):
                    # Create a relative path to the image file
                    rel_path = f"{class_name}/{split}/{label}/{fname}"
                    
                    # Write the relative path and label to the output file
                    f.write(f"{rel_path} {label}\n")

# Print a success message when done
print("✅ clean_labels.txt created.")
