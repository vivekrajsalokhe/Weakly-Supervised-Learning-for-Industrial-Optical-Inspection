# merge_dagm_dataset.py
# This script merges Class1–Class6 train/test data into unified train/ and test/ folders

import os
import shutil

def merge_all_classes(base_path="./data", target_base="./", class_range=range(1, 7)):
    # Create train/0, train/1, test/0, test/1 folders in the target base
    for split in ['Train', 'Test']:
        for label in ['0', '1']:
            os.makedirs(os.path.join(target_base, split.lower(), label), exist_ok=True)

    # For each class folder (Class1 to Class6)
    for i in class_range:
        class_path = os.path.join(base_path, f"Class{i}")
        for split in ['Train', 'Test']:
            for label in ['0', '1']:
                src_folder = os.path.join(class_path, split, label)
                dst_folder = os.path.join(target_base, split.lower(), label)
                # Copy each image to the global folder with class index as prefix
                if os.path.exists(src_folder):
                    for fname in os.listdir(src_folder):
                        src = os.path.join(src_folder, fname)
                        dst = os.path.join(dst_folder, f"class{i}_{fname}")
                        shutil.copyfile(src, dst)

    print("✅ Dataset merged into global train/ and test/ folders")

# Run merging if this file is executed directly
if __name__ == "__main__":
    merge_all_classes()
