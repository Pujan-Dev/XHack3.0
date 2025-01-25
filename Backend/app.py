from flask import Flask, jsonify, request, session,render_template
from flask_session import Session
from flask_cors import CORS
import asyncio
import aiohttp
from aiohttp import ClientSession
import requests
import re

app = Flask(__name__)
CORS(app)


# Configure session to use filesystem (store session data on the server)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn


# GNews API details
API_KEY = 'ff63db4f1692485dd6127d9c911e0faf'
GNEWS_API_URL = 'https://gnews.io/api/v4/top-headlines'

# Default list of countries to fetch news from
default_countries = ['us', 'in', 'ca', 'gb', 'au']

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
                articles = []
                for article in news_data.get("articles", []):
                    articles.append({
                        "title": article["title"],
                        "date": article["publishedAt"],
                        "content": article["content"],
                        "country": country  # Add country to the article
                    })
                return articles
            else:
                print(f"Failed to fetch news for {country}, status code: {response.status}")
                return []
    except Exception as e:
        print(f"Error fetching news for {country}: {str(e)}")
        return []
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news', methods=['GET'])
async def get_news():
    try:
        # Get query parameters
        keyword = request.args.get('keyword', 'agriculture')
        lang = request.args.get('lang', 'en')
        max_results = int(request.args.get('max', 7))

        # Create a list of tasks for fetching news for each country
        async with ClientSession() as session:
            tasks = [fetch_news_for_country(session, country, keyword, lang, max_results) for country in default_countries]

            # Run all tasks concurrently and gather the results
            results = await asyncio.gather(*tasks)

        # Flatten the list of lists into a single list
        all_articles = [article for country_articles in results for article in country_articles]

        return jsonify(all_articles)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test', methods=['GET'])
def test():
    return "Server is running!"

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
