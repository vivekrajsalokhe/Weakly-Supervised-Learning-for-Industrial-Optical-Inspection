# requirements.txt
# This file lists all required packages to run the project

torch
torchvision
matplotlib
scikit-learn
pandas
Pillow


# inference_ui.py
# A simple command-line interface to test predictions on new images

import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import sys

# Load the trained model
def load_model(model_path):
    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 2)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# Preprocess input image
def preprocess_image(image_path):
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=3),
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])
    image = Image.open(image_path).convert("L")
    return transform(image).unsqueeze(0)  # Add batch dimension

# Predict label for image
def predict(model, image_tensor):
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)
        return "Defective" if predicted.item() == 1 else "Non-Defective"

# Main function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python inference_ui.py <model_path> <image_path>")
        sys.exit(1)

    model_path = sys.argv[1]
    image_path = sys.argv[2]

    model = load_model(model_path)
    image_tensor = preprocess_image(image_path)
    result = predict(model, image_tensor)
    print(f"Prediction: {result}")


