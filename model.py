from flask import Flask, render_template, request, jsonify, send_from_directory
import torch
from efficientnet_pytorch import EfficientNet
from torchvision import transforms
from PIL import Image
import os

# Initialize Flask app
app = Flask(__name__, template_folder=os.path.dirname(os.path.abspath(__file__)))

# Path to the current directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the model (update with your actual model loading code)
MODEL_PATH = 'tool_recognition_efficientnet.pth'  # Ensure the file format matches your updated model
class_labels = ['Gasoline Can', 'Hammer', 'Pebble', 'Pliers', 'Rope', 'Screw Driver', 'Tool Box', 'Wrench']

# Load pre-trained EfficientNet model (efficientnet-b0 is used here, you can change it if needed)
model = EfficientNet.from_pretrained('efficientnet-b0')

# Modify the final fully connected layer to match the number of classes
model._fc = torch.nn.Linear(in_features=model._fc.in_features, out_features=len(class_labels))

# Load model weights
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
model.eval()  # Set model to evaluation mode

# Define image transform
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

@app.route('/')
def index():
    return render_template('index.html')  # Flask will now look in the current directory

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Open and transform the image
        img = Image.open(file.stream).convert('RGB')
        img = transform(img).unsqueeze(0)  # Add batch dimension

        # Perform prediction
        with torch.no_grad():
            output = model(img)
            _, predicted_class = torch.max(output, 1)

        # Map the predicted class to the corresponding tool name
        predicted_tool = class_labels[predicted_class.item()]
        return jsonify({'prediction': predicted_tool})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# To serve all files (CSS, JS, Images, etc.) directly from the current directory
@app.route('/<filename>')
def serve_file(filename):
    return send_from_directory(CURRENT_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
