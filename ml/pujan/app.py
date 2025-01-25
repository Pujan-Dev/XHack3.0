from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64
from io import BytesIO

app = Flask(__name__)
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Load your trained model
model = tf.keras.models.load_model('best_model.h5')

# Function to preprocess the image before passing it to the model
def preprocess_image(image, target_size=(50, 50)):
    image = image.resize(target_size)  # Resize to match the input size of the model
    image = np.array(image) / 255.0  # Normalize pixel values
    if image.shape[-1] != 3:  # Ensure the image has 3 channels (RGB)
        image = np.stack((image,) * 3, axis=-1)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'image' not in data:
        return jsonify({'error': 'No image provided.'})

    image_data = data['image']
    
    # Decode the base64 image
    image_data = image_data.split(",")[1]  # Remove the "data:image/jpeg;base64," part
    image_bytes = base64.b64decode(image_data)
    
    try:
        # Open the image
        image = Image.open(BytesIO(image_bytes))
        processed_image = preprocess_image(image)
        
        # Make prediction
        prediction = model.predict(processed_image)
        predicted_class = np.argmax(prediction, axis=1)[0]  # Get the class index
        confidence = prediction[0][predicted_class]  # Get confidence score

        return jsonify({
            'predicted_class': alpha[predicted_class],
            'confidence': float(confidence)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
