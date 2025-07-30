🛠️ Industrial Defect Detector – Weakly Supervised Learning Project
This project is a full pipeline for detecting surface defects in industrial components using deep learning and computer vision. It uses weakly supervised learning on the DAGM 2007 dataset and provides both training scripts and a modern web-based interface.

🔍 What It Does
✅ Classifies images and videos as “Defective” or “Non-Defective”

✅ Uses a ResNet18 model trained on industrial surface images

✅ Provides a beautiful Flask-based UI for user interaction

✅ Works with both images and videos

✅ Shows how many frames in a video contain defects

🧠 How It Works
The model is based on ResNet18, pre-trained on ImageNet and fine-tuned for binary classification.

For video inputs, it processes every Nth frame (default: every 15th), classifies each frame, and summarizes the results.

For image inputs, it runs inference immediately and displays the result.

📂 Dataset
This project uses the DAGM 2007 dataset for training and evaluation. It contains six different industrial textures with both defect-free and defective samples.

📦 Dataset Details:

Name: DAGM 2007 (Deutsche Arbeitsgemeinschaft für Mustererkennung)

Classes: 6 (Class1 to Class6)

Format: Grayscale PNG images with label files

Labels: 0 = Non-Defective, 1 = Defective

🔗 Download Link:
You can download the dataset here: https://zenodo.org/records/12750201

Once downloaded, place the dataset folders inside the data/ directory as shown in the structure below.

💻 Technologies Used
Python, PyTorch, OpenCV, Flask

PIL for image handling

HTML + CSS for frontend

DAGM 2007 dataset

📁 Project Structure
project/
│
├── app.py                # Flask application
├── main.py               # Runs training
├── scripts/              # Model training, data loaders
├── data/                 # Organized industrial image data
├── templates/index.html  # UI layout
├── static/uploads/       # Stores uploaded media
├── models/               # Trained models saved here
├── utils/                # Helper scripts
└── requirements.txt
🚀 How to Run
1. Install dependencies:
pip install -r requirements.txt

2. Train the model :
python main.py

3. Start the web app:
python app.py
4. Open your browser at:
http://127.0.0.1:5000

🎥 Video Support
For videos, the app samples frames using OpenCV and runs predictions on them individually, then shows how many frames were predicted as defective.
