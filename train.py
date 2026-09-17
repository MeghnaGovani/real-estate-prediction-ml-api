import pandas as pd
import numpy as np
import os
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor

# 1. Load dataset
df = pd.read_csv('real_estate.csv')

# Features for clustering
X_spatial = df[['latitude', 'longitude', 'sqft', 'bedrooms']]

# 2. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_spatial)

# 3. Train K-Means Clustering (3 hot zones)
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster_id'] = kmeans.fit_predict(X_scaled)

# 4. Train Random Forest using features + cluster_id
X_rf = df[['latitude', 'longitude', 'sqft', 'bedrooms', 'cluster_id']]
y = df['price']

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_rf, y)

# 5. Export artifacts to /models directory
os.makedirs('models', exist_ok=True)  # Creates directory if it doesn't exist

joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(kmeans, 'models/kmeans_model.pkl')
joblib.dump(rf_model, 'models/rf_model.pkl')

print("Models and Scaler trained and saved successfully!")