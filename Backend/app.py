from flask import Flask, jsonify, request, session
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import sqlite3
import requests
import re

app = Flask(__name__)
CORS(app)

#sujal part
class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 
               'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
               'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
               'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
               'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
               'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
               'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
               'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
               'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot',
               'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
               'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']


def predict(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(255, 255))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)
    return predicted_class, confidence
#end of sujal part raoute is defiend below 


#start of pujan part 
label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'blank']
def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 50, 50, 1)
    return feature / 255.0

# Initialize camera
camera = cv2.VideoCapture(0)  # Adjust the camera index if necessary

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            app.logger.error("Failed to read frame from camera. Retrying...")
            continue  # Retry reading the frame
        else:
            app.logger.info("Frame captured")

            # Crop and process frame
            cv2.rectangle(frame, (0, 40), (300, 300), (0, 165, 255), 1)
            crop_frame = frame[40:300, 0:300]
            crop_frame_gray = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
            crop_frame_resized = cv2.resize(crop_frame_gray, (50, 50))
            crop_frame_normalized = extract_features(crop_frame_resized)

            # Prediction
            pred = model.predict(crop_frame_normalized)
            prediction_label = label[pred.argmax()]

            # Display prediction
            cv2.rectangle(frame, (0, 0), (300, 40), (0, 165, 255), -1)
            if prediction_label == 'blank':
                cv2.putText(frame, " ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                accu = "{:.2f}".format(np.max(pred) * 100)
                cv2.putText(frame, f'{prediction_label}  {accu}%', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                app.logger.error("Failed to encode frame")
                continue
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#end of pujan part 
# Configure session to use filesystem (store session data on the server)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'your_secret_key'
Session(app)

# SQLite database setup
DATABASE = 'geeklogin.db'

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


# Route to handle user registration (signup)
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
#starting route for sujal part
@app.route('/predict', methods=['POST'])
def handle_predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Ensure the upload folder exists
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        file.save(filepath)

        # Get prediction
        predicted_class, confidence = predict(filepath)

        return jsonify({
            "predicted_class": predicted_class,
            "confidence": confidence,
            "image_path": filepath
        })
    else:
        return jsonify({"error": "Invalid file format"}), 400
    
#end route for sujal part




#starting route for pujan part

if __name__ == '__main__':
    init_db()  # Ensure database is initialized before starting the app
    app.run(debug=True)
