import sqlite3
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_PATH = 'database.db'

# Load artifacts
scaler = joblib.load('models/scaler.pkl')
kmeans = joblib.load('models/kmeans_model.pkl')
rf_model = joblib.load('models/rf_model.pkl')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL, longitude REAL, sqft REAL,
            bedrooms INTEGER, cluster_id INTEGER, predicted_price REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    lat = float(data['latitude'])
    lng = float(data['longitude'])
    sqft = float(data['sqft'])
    beds = int(data['bedrooms'])

    # Preprocess & Predict
    raw_input = np.array([[lat, lng, sqft, beds]])
    scaled_input = scaler.transform(raw_input)
    cluster_id = int(kmeans.predict(scaled_input)[0])

    rf_input = np.array([[lat, lng, sqft, beds, cluster_id]])
    pred_price = float(rf_model.predict(rf_input)[0])

    # DB Logging
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO predictions (latitude, longitude, sqft, bedrooms, cluster_id, predicted_price)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (lat, lng, sqft, beds, cluster_id, round(pred_price, 2)))
    conn.commit()
    conn.close()

    return jsonify({
        'status': 'success',
        'cluster_id': cluster_id,
        'predicted_price': round(pred_price, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)