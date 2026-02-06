import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# CHANGE THESE ONLY
DATASET_PATH = "../datasets/heart.csv"
FEATURES = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"]
TARGET = "target"
MODEL_NAME = "heart.pkl"

# Load dataset
df = pd.read_csv(DATASET_PATH)

X = df[FEATURES]
y = df[TARGET]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open(MODEL_NAME, "wb"))

print(f"{MODEL_NAME} trained and saved")
