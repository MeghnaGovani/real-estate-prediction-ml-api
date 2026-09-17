import os
import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# 1. Load your local dataset file directly
df = pd.read_csv('real_estate.csv')

# Define features and target column
feature_cols = ["latitude", "longitude", "sqft", "bedrooms"]
target_col = "price"

X_spatial = df[feature_cols]

# 2. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_spatial)

# 3. Train K-Means Clustering (3 hot zones)
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster_id"] = kmeans.fit_predict(X_scaled)

# 4. Train Random Forest using features + cluster_id
X_rf = df[feature_cols + ["cluster_id"]]
y = df[target_col]

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_rf, y)

# 5. Export artifacts to /models directory
os.makedirs("models", exist_ok=True)

joblib.dump(scaler, "models/scaler.pkl")
joblib.dump(kmeans, "models/kmeans_model.pkl")
joblib.dump(rf_model, "models/rf_model.pkl")

print("Models and Scaler trained and saved successfully!")