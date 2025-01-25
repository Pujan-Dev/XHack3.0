from flask import Flask, jsonify, request, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import sqlite3
import requests
import re

app = Flask(__name__)
CORS(app)

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
    conn = get_db_connection()
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

# GNews API details
API_KEY = 'ff63db4f1692485dd6127d9c911e0faf'
GNEWS_API_URL = 'https://gnews.io/api/v4/top-headlines'

@app.route('/news', methods=['GET'])
def get_news():
    try:
        keyword = request.args.get('keyword', 'natural disaster')
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
            news_data = response.json()
            simplified_articles = [
                {
                    "title": article["title"],
                    "date": article["publishedAt"],
                    "content": article["content"]
                }
                for article in news_data.get("articles", [])
            ]
            return jsonify(simplified_articles)
        else:
            return jsonify({'error': 'Failed to fetch news'}), response.status_code

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


if __name__ == '__main__':
    init_db()  # Ensure database is initialized before starting the app
    app.run(debug=True)
