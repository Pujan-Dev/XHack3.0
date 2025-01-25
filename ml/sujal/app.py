import numpy as np
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
from io import BytesIO
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from flask_cors import CORS  # Flask-CORS for handling CORS
from tensorflow.keras import backend as K  # To clear session

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow all origins

# Clear the previous TensorFlow session to avoid conflicts
K.clear_session()

# Load the pre-trained Keras model
try:
    model = load_model('./Plant Disease Detection_fixed.h5')
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    exit()

# Define the class labels (modify this according to your model's output)
class_labels = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot",
    "Corn_(maize)___Common_rust",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites_Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

# Function to prepare the image
def prepare_image(img):
    img = img.convert('RGB')  # Ensure image is in RGB mode
    img = img.resize((224, 224))  # Resize the image to the input size expected by your model
    img_array = np.array(img)  # Convert image to numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Apply preprocessing if needed
    return img_array

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Open the image file as BytesIO
        img = Image.open(BytesIO(file.read()))  # Use the BytesIO to open the image
        img_array = prepare_image(img)

        # Make the prediction
        prediction = model.predict(img_array)
        predicted_class = class_labels[np.argmax(prediction)]
        confidence = float(np.max(prediction))  # Confidence of the prediction

        return jsonify({'prediction': predicted_class, 'confidence': confidence})

    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
