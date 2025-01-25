from flask import Flask, jsonify, request
from flask_cors import CORS
import asyncio
from aiohttp import ClientSession
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from PIL import Image
import base64
from io import BytesIO
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)
CORS(app)

# GNews API details
API_KEY = '2560aebc8c041ca424aa4fe71e481a5b'
GNEWS_API_URL = 'https://gnews.io/api/v4/top-headlines'

# Default list of countries to fetch news from
default_countries = ['us', 'in', 'ca', 'gb', 'au']

# Function to fetch news asynchronously for a given country
async def fetch_news_for_country(session: ClientSession, country: str, keyword: str, lang: str, max_results: int):
    params = {
        'q': keyword,
        'lang': lang,
        'country': country,
        'token': API_KEY,
        'max': max_results
    }

    try:
        async with session.get(GNEWS_API_URL, params=params) as response:
            if response.status == 200:
                news_data = await response.json()
                return [
                    {
                        "title": article["title"],
                        "date": article["publishedAt"],
                        "content": article["content"],
                        "country": country
                    }
                    for article in news_data.get("articles", [])
                ]
            else:
                print(f"Failed to fetch news for {country}, status code: {response.status}")
                return []
    except Exception as e:
        print(f"Error fetching news for {country}: {str(e)}")
        return []

# API endpoint to fetch news
@app.route('/news', methods=['GET'])
async def get_news():
    keyword = request.args.get('keyword', 'agriculture')
    lang = request.args.get('lang', 'en')
    max_results = int(request.args.get('max', 7))

    async with ClientSession() as session:
        tasks = [fetch_news_for_country(session, country, keyword, lang, max_results) for country in default_countries]
        results = await asyncio.gather(*tasks)

    all_articles = [article for country_articles in results for article in country_articles]
    return jsonify(all_articles)

# Test endpoint to check server status
@app.route('/test', methods=['GET'])
def test():
    return "Server is running!"
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Load your trained model
model = tf.keras.models.load_model('/home/sujal/hacker/XHack3.0/Backend/best_model.h5')

# Function to preprocess the image before passing it to the model
def preprocess_image(image, target_size=(50, 50)):
    image = image.resize(target_size)  # Resize to match the input size of the model
    image = np.array(image) / 255.0  # Normalize pixel values
    if image.shape[-1] != 3:  # Ensure the image has 3 channels (RGB)
        image = np.stack((image,) * 3, axis=-1)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


@app.route('/api/predict', methods=['POST'])
def predict():
    if not request.json or 'image' not in request.json:
        return jsonify({'error': 'No image provided.'}), 400  # Return 400 for bad request

    image_data = request.json['image']
    
    # Decode the base64 image
    try:
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
            'predicted_class': alpha[predicted_class],
            'confidence': float(confidence)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return 500 for internal server error

#sujal's part
# Define the path for your trained model
MODEL_PATH = '/home/sujal/hacker/XHack3.0/Backend/trained_model.keras'

# Class names for prediction
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

# Image size for preprocessing
IMAGE_SIZE = 255

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

# Route to handle requests
@app.route('/api/predict_sujal', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Check if file part exists in the request
            if 'file' not in request.files:
                return jsonify({'message': 'No file part in request.'})

            file = request.files['file']

            # Check if the filename is empty
            if file.filename == '':
                return jsonify({'message': 'No selected file.'})

            # Validate file extension (allow only png, jpg, jpeg)
            if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in {'png', 'jpg', 'jpeg'}:
                return jsonify({'message': 'Invalid file type.'})

            # Save the file securely
            filename = secure_filename(file.filename)
            static_dir = os.path.join(os.getcwd(), "static")
            os.makedirs(static_dir, exist_ok=True)
            filepath = os.path.join(static_dir, filename)
            file.save(filepath)
            print(f"File saved to {filepath}")

            # Load and preprocess the image
            img = tf.keras.preprocessing.image.load_img(filepath, target_size=(IMAGE_SIZE, IMAGE_SIZE))
            predicted_class, confidence = predict(img, model, class_names)

            if predicted_class is None:
                return jsonify({'message': 'Prediction failed.'})

            return jsonify({
                # 'image_path': f"static/{filename}",
                'actual_label': predicted_class,
                'predicted_label': predicted_class,
                'confidence': float( confidence)
            })
        except Exception as e:
            print(f"Error during request handling: {e}")
            return jsonify({'message': f"An error occurred: {e}"})

    return jsonify({'message': 'Upload an image'})

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
