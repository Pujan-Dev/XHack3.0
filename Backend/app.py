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

app = Flask(__name__)
CORS(app)

# GNews API details
API_KEY = '65a30a9096b63f0b6efb68cb5b93b631'
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
model = tf.keras.models.load_model('best_model.h5')

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



if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
