from flask import Flask, jsonify, request
from flask_cors import CORS
import asyncio
from aiohttp import ClientSession

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


if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
