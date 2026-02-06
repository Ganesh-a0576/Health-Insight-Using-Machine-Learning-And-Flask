import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("../datasets/liver.csv")

# Encode categorical column
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})

# Encode target column
df["Dataset"] = df["Dataset"].map({1: 1, 2: 0})

# Convert all columns to numeric
df = df.apply(pd.to_numeric, errors="coerce")

# Fill missing values
df.fillna(df.mean(), inplace=True)

# Split features and target
X = df.drop(columns=["Dataset"])
y = df["Dataset"].astype(int)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open("liver.pkl", "wb"))

print("Liver model trained successfully")
