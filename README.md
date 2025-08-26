# XHack3.0

XHack3.0 is a full-stack web application integrating multiple functionalities into a single platform:

1. **News Dashboard** – Browse latest news by category.
2. **Human Sign Detector** – ML-based human gesture/sign detection.
3. **Crop Disease Detector** – ML-based crop disease detection from images.

This platform combines backend APIs, frontend dashboard, and machine learning modules into a seamless, modular architecture.

---

## 🚀 Features

- **News**: Real-time news aggregation across multiple categories.
- **Human Sign Detection**: Detect human gestures using pre-trained ML models.
- **Crop Disease Detection**: Upload crop images to automatically identify diseases.
- **Responsive Web UI**: Interactive and user-friendly interface.
- **Modular Architecture**: Clear separation of backend, frontend, and ML modules.
- **Easy to Extend**: Add new ML models or features without breaking the system.

---

## 🗂️ Project Structure

```

XHack3.0/
│
├── backend/          # API server, ML integration, database logic
├── frontend/         # Web dashboard (React / Vue / etc.)
├── ml/               # Machine learning models and scripts
│   ├── human\_sign/   # Human gesture detection model
│   └── crop\_disease/ # Crop disease detection model
├── static/           # Images, CSS, JS
├── requirements.txt  # Python dependencies
├── package.json      # Node.js dependencies
└── README.md

````

---

## 🛠️ Installation

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm/yarn
- Git
- Optional: Virtual environment for Python

### Setup Steps

1. **Clone the repository**

```bash
git clone https://github.com/Pujan-Dev/XHack3.0.git
cd XHack3.0
````

2. **Backend**

```bash
cd backend
pip install -r requirements.txt
python app.py   # Start backend server
```

3. **Frontend**

```bash
cd ../frontend
npm install
npm run dev    # or npm start
```

4. **Machine Learning**

* Ensure the ML models in `ml/human_sign` and `ml/crop_disease` are present.
* Install ML dependencies if any:

```bash
pip install -r ml/requirements.txt
```

5. **Access the App**

* Open your browser: `http://localhost:3000`

---

## 👥 Team

| Name          | Role           |
| ------------- | -------------- |
| Pujan Neupane | ML + Fullstack |
| Sujal Karki   | ML + Backend   |
| Roshan Panthi | Frontend       |
| Rabin Kattel  | Backend        |

