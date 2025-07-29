# Clean label files in DAGM dataset by removing entries with label '2'

import os

# Loop through Class1 to Class6 folders
for i in range(1, 7):
    path = f"./data/Class{i}/Label/Labels.txt"
    
    # Skip if label file doesn't exist
    if not os.path.exists(path):
        continue

    # Read all lines from the label file
    with open(path, 'r') as f:
        lines = f.readlines()

    # Write back only the header and valid lines (exclude lines with label '2')
    with open(path, 'w') as f:
        f.write(lines[0])  # keep header
        for line in lines[1:]:
            if '\t2\t' not in line:
                f.write(line)

    print(f"✅ Cleaned label file: {path}")
