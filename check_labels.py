# Import required libraries
from pathlib import Path
import torch
from torchvision import datasets, transforms

# Load dataset from './train' folder and apply tensor transformation
dataset = datasets.ImageFolder(
    root="./train",  # Folder structure should be train/0/, train/1/ etc.
    transform=transforms.ToTensor()
)

# Extract all class labels from the dataset
targets = torch.tensor(dataset.targets)

# Display the unique labels in the dataset (e.g., [0, 1])
print("Unique labels in dataset:", torch.unique(targets))
