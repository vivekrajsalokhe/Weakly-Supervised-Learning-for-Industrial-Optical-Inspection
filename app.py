# Flask app for image/video-based defect detection using a ResNet18 model
from flask import Flask, render_template, request
import torch
from torchvision import transforms, models
from PIL import Image
import os
import cv2

# Setup Flask and file upload directory
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Setup device and load trained model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(weights='IMAGENET1K_V1')
model.fc = torch.nn.Linear(model.fc.in_features, 2)
model.load_state_dict(torch.load("models/best_model.pth", map_location=device))
model.to(device)
model.eval()

# Image preprocessing pipeline
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Function to predict defects from video frames
def predict_video_defects(video_path, model, transform, device, frame_sample_rate=15):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    defect_count = 0
    total_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_sample_rate == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb).convert("L")
            input_tensor = transform(pil_image).unsqueeze(0).to(device)
            with torch.no_grad():
                output = model(input_tensor)
                _, pred = torch.max(output, 1)
                if pred.item() == 1:
                    defect_count += 1
            total_frames += 1
        frame_count += 1

    cap.release()
    return defect_count, total_frames

# Route for handling file uploads and predictions
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    filename = None
    media_type = None

    if request.method == "POST":
        file = request.files["media"]
        if file:
            filename = file.filename
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)

            ext = filename.lower()
            if ext.endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                media_type = "image"
                try:
                    image = Image.open(save_path).convert("L")
                    image = transform(image).unsqueeze(0).to(device)
                    with torch.no_grad():
                        outputs = model(image)
                        _, pred = torch.max(outputs, 1)
                        label = "Defective" if pred.item() == 1 else "Non-Defective"
                        prediction = f"Prediction: {label}"
                except Exception:
                    prediction = "❌ Error processing image."

            elif ext.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                media_type = "video"
                defect_count, total = predict_video_defects(save_path, model, transform, device)
                prediction = f"📹 Processed video — {defect_count} out of {total} frames show defects."
            else:
                prediction = "❗ Unsupported file format."

    return render_template("index.html", prediction=prediction, filename=filename, media_type=media_type)

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
