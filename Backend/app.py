from flask import Flask, jsonify, request, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import sqlite3
import asyncio
import aiohttp
from aiohttp import ClientSession
import requests
import re

app = Flask(__name__)
CORS(app)

# Configure session to use filesystem (store session data on the server)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'your_secret_key'
Session(app)

# SQLite database setup
DATABASE = 'vault.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows column access by name
    return conn

# Initialize database with a table
def init_db():
    try:
        conn = get_db_connection()
        print("Connected to database...")
        conn.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Database initialization failed: {e}")




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

@app.route('/news', methods=['GET'])
async def get_news():
    try:
        # Get query parameters
        keyword = request.args.get('keyword', 'natural disaster')
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


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Validate inputs
    if not username or not password or not email:
        return jsonify({'message': 'Please fill out all fields!'}), 400
    if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return jsonify({'message': 'Invalid email address!'}), 400
    if not re.match(r'^[A-Za-z0-9]+$', username):
        return jsonify({'message': 'Username must contain only letters and numbers!'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username = ?', (username,))
    account = cursor.fetchone()

    if account:
        conn.close()
        return jsonify({'message': 'Account already exists!'}), 400

    hashed_password = generate_password_hash(password)
    cursor.execute('INSERT INTO accounts (username, password, email) VALUES (?, ?, ?)', 
                   (username, hashed_password, email))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User registered successfully!'}), 201


# Route to handle user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM accounts WHERE username = ?', (username,))
    account = cursor.fetchone()

    if account and check_password_hash(account['password'], password):
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        conn.close()
        return jsonify({'message': 'Login successful!', 'username': username}), 200
    else:
        conn.close()
        return jsonify({'message': 'Incorrect username or password!'}), 401


# Route to handle user logout
@app.route('/logout', methods=['POST'])
def logout():
    if 'loggedin' in session:
        session.clear()
        return jsonify({'message': 'Logged out successfully!'}), 200
    return jsonify({'message': 'No active session!'}), 400
# #starting route for sujal part
# @app.route('/predict', methods=['POST'])
# def handle_predict():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file part"}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

#         # Ensure the upload folder exists
#         os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

#         file.save(filepath)

#         # Get prediction
#         predicted_class, confidence = predict(filepath)

#         return jsonify({
#             "predicted_class": predicted_class,
#             "confidence": confidence,
#             "image_path": filepath
#         })
#     else:
#         return jsonify({"error": "Invalid file format"}), 400
    
#end route for sujal part




#starting route for pujan part
if __name__ == '__main__':
    init_db()
    print("Starting Flask app...")
    app.run(debug=True)

