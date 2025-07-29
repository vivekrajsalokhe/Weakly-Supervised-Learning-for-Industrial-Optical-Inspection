# prepare_dagm_dataset.py
# Prepares DAGM dataset by organizing Class1–Class6 into structured Train/Test folders by label

import os
import shutil
import random
from PIL import Image
from tqdm import tqdm

def prepare_class_dataset(class_dir, seed=42, split_ratio=0.8):
    # Locate and validate the label file inside the class directory
    label_file = os.path.join(class_dir, 'Label', 'Labels.txt')
    if not os.path.exists(label_file):
        print(f"Label file missing in {class_dir}")
        return

    # Read and parse the label file, skipping the header
    with open(label_file, 'r') as f:
        lines = f.readlines()[1:]

    # Organize image filenames by defect label (0 = non-defective, 1 = defective)
    data = {0: [], 1: []}
    for line in lines:
        parts = line.strip().split('\t')
        try:
            label = int(parts[1])
            img_file = parts[2]
            if label in (0, 1):
                data[label].append(img_file)
            else:
                print(f"⚠️ Skipping unexpected label {label} in {class_dir}: {parts}")
        except Exception as e:
            print(f"⚠️ Skipping malformed line: {line.strip()} ({e})")

    # Randomly shuffle the image filenames for each label class
    random.seed(seed)
    for label in data:
        random.shuffle(data[label])

    # Create the folder structure for Train/Test splits per label
    for split in ['Train', 'Test']:
        for label in ['0', '1']:
            os.makedirs(os.path.join(class_dir, split, label), exist_ok=True)

    # Split the images and copy them into the corresponding folders
    for label, img_list in data.items():
        split_idx = int(len(img_list) * split_ratio)
        train_imgs = img_list[:split_idx]
        test_imgs = img_list[split_idx:]

        for img_name in train_imgs:
            src = os.path.join(class_dir, img_name)
            dst = os.path.join(class_dir, 'Train', str(label), os.path.basename(img_name))
            if os.path.exists(src):
                shutil.copyfile(src, dst)
            else:
                print(f"⚠️ Missing image: {src}")

        for img_name in test_imgs:
            src = os.path.join(class_dir, img_name)
            dst = os.path.join(class_dir, 'Test', str(label), os.path.basename(img_name))
            if os.path.exists(src):
                shutil.copyfile(src, dst)
            else:
                print(f"⚠️ Missing image: {src}")

    # Print final summary for the class folder
    print(f"✅ {class_dir} prepared with {len(data[0]) + len(data[1])} total images")

if __name__ == "__main__":
    # Loop through Class1 to Class6 and prepare each dataset
    base_path = "./data"
    for i in range(1, 7):
        class_dir = os.path.join(base_path, f"Class{i}")
        if os.path.exists(class_dir):
            prepare_class_dataset(class_dir)
        else:
            print(f"Class{i} folder not found")
