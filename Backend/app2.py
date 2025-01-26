from flask import Flask, jsonify, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Constants
MODEL_PATH = '/home/sujal/hacker/XHack3.0/Backend/trained_model.keras'
IMAGE_SIZE = 255
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
STATIC_DIR = os.path.join(os.getcwd(), "static")

# Class names for predictions
class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]

# Load the model
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# Global model initialization
model = load_model()

# Function to preprocess the image and make predictions
def predict(img, model, class_names):
    try:
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Add batch dimension
        predictions = model.predict(img_array)
        predicted_class = class_names[np.argmax(predictions[0])]  # Get the predicted class
        confidence = round(100 * np.max(predictions[0]), 2)  # Confidence in the prediction
        return predicted_class, confidence
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None, None

# Helper function to validate file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to handle predictions
@app.route('/api/predict_sujal', methods=['POST'])
def predict_sujal():
    if model is None:
        return jsonify({'message': 'Model loading failed.'})

    try:
        # Check if file part exists in the request
        if 'file' not in request.files:
            return jsonify({'message': 'No file part in request.'})

        file = request.files['file']

        # Check if the filename is empty
        if file.filename == '':
            return jsonify({'message': 'No selected file.'})

        # Validate file extension
        if not allowed_file(file.filename):
            return jsonify({'message': 'Invalid file type. Only png, jpg, jpeg allowed.'})

        # Save the file securely
        filename = secure_filename(file.filename)
        os.makedirs(STATIC_DIR, exist_ok=True)
        filepath = os.path.join(STATIC_DIR, filename)
        file.save(filepath)
        print(f"File saved to {filepath}")

        # Load and preprocess the image
        img = tf.keras.preprocessing.image.load_img(filepath, target_size=(IMAGE_SIZE, IMAGE_SIZE))
        predicted_class, confidence = predict(img, model, class_names)

        if predicted_class is None:
            return jsonify({'message': 'Prediction failed.'})

        return jsonify({
            'actual_label': predicted_class,
            'predicted_label': predicted_class,
            'confidence': float(confidence)
        })
    except Exception as e:
        print(f"Error during request handling: {e}")
        return jsonify({'message': f"An error occurred: {e}"})

# Route for testing the API
@app.route('/')
def home():
    return jsonify({'message': 'Upload an image to /api/predict_sujal for prediction.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
