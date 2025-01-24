from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'ff63db4f1692485dd6127d9c911e0faf'
GNEWS_API_URL = 'https://gnews.io/api/v4/top-headlines'

@app.route('/')
def home():
    return "Welcome to the GNews API Service!"

@app.route('/news', methods=['GET'])
def get_news():
    try:
        keyword = request.args.get('keyword', 'disaster')
        lang = request.args.get('lang', 'en')
        country = request.args.get('country', 'us')
        max_results = request.args.get('max', 7)

        params = {
            'q': keyword,
            'lang': lang,
            'country': country,
            'token': API_KEY,
            'max': max_results
        }

        response = requests.get(GNEWS_API_URL, params=params)

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'Failed to fetch news'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
