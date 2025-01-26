from flask import Flask, jsonify, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
from io import BytesIO
from werkzeug.utils import secure_filename
import os

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Constants
ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MODEL_PATH = 'best_model.h5'

# Load the trained model
def load_model():
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Model loaded successfully!")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

model = load_model()

# Function to preprocess the image before passing it to the model
def preprocess_image(image, target_size=(50, 50)):
    image = image.resize(target_size)  # Resize to match the input size of the model
    image = np.array(image) / 255.0  # Normalize pixel values
    if image.shape[-1] != 3:  # Ensure the image has 3 channels (RGB)
        image = np.stack((image,) * 3, axis=-1)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# API route for making predictions
@app.route('/api/predict', methods=['POST'])
def predict():
    if not request.json or 'image' not in request.json:
        return jsonify({'error': 'No image provided.'}), 400  # Return 400 for bad request

    image_data = request.json['image']
    
    try:
        # Decode the base64 image
        image_data = image_data.split(",")[1]  # Remove the "data:image/jpeg;base64," part
        image_bytes = base64.b64decode(image_data)

        # Open the image
        image = Image.open(BytesIO(image_bytes))
        processed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=1)[0]  # Get the class index
        confidence = prediction[0][predicted_class]  # Get confidence score

        return jsonify({
            'predicted_class': ALPHA[predicted_class],
            'confidence': float(confidence)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return 500 for internal server error

if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0', port=8000)
