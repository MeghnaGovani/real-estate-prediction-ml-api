# Smart Real Estate & Neighborhood Price Predictor 🏡🤖

A Machine Learning-powered REST API and interactive web application designed to segment properties into geographic neighborhood hot zones using **K-Means Clustering** and predict property valuations using **Random Forest Regression**. 

Built with **Flask**, **SQLite**, **Scikit-Learn**, and vanilla **HTML5/CSS3/JavaScript**.

---

## 📌 Features

- **Spatial Hotspot Clustering:** Employs unsupervised **K-Means Clustering** on geospatial and property metadata (latitude, longitude, sqft, bedrooms) to group real estate into distinct market zones.
- **Valuation Engine:** Uses a **Random Forest Regressor** trained on property features and assigned `cluster_id` vectors for accurate price prediction.
- **RESTful API Backend:** Clean **Flask** web framework exposing JSON REST endpoints (`/api/predict`).
- **Audit Logging:** Automatically logs user predictions, input parameters, and output cluster IDs in a local **SQLite** database.
- **Asynchronous Frontend UI:** Lightweight, responsive user interface utilizing JS `fetch()` for dynamic UI updates without page reloads.

---

## 📁 Repository Structure

```text
real_estate_prediction/
├── app.py                  # Flask application server & API routes
├── train.py                # Pipeline script to train and export ML models
├── real_estate.csv         # Raw housing dataset
├── database.db             # SQLite database for prediction query logging
├── models/
│   ├── scaler.pkl          # Pre-trained StandardScaler model
│   ├── kmeans_model.pkl    # Pre-trained K-Means clustering model
│   └── rf_model.pkl        # Pre-trained Random Forest regression model
├── static/
│   ├── css/
│   │   └── style.css       # Custom layout and UI styles
│   └── js/
│       └── main.js         # Frontend fetch client and DOM handling
├── templates/
│   └── index.html          # Web dashboard interface
├── .gitignore              # Ignored files and local database rules
└── README.md               # Project documentation

🚀 Getting Started
1. Clone the Repository
Bash
git clone [https://github.com/MeghnaGovani/real-estate-prediction-ml-api.git](https://github.com/MeghnaGovani/real-estate-prediction-ml-api.git)
cd real-estate-prediction-ml-api
2. Run the Model Training Pipeline
Bash
python3 train.py
3. Start the Web App
Bash
python3 app.py
Open your browser and navigate to http://127.0.0.1:5000.

🔌 API Endpoint Documentation
Predict Property Price
URL: /api/predict

Method: POST

Headers: Content-Type: application/json

JSON
{
  "latitude": 24.98208,
  "longitude": 121.53951,
  "sqft": 1200,
  "bedrooms": 3
}
🛠️ Tech Stack
Machine Learning: Scikit-Learn, Pandas, NumPy, Joblib

Backend: Python, Flask, SQLite3

Frontend: HTML5, CSS3, JavaScript (Fetch API)