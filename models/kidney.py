import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("../datasets/kidney.csv")

# Drop ID column
df.drop(columns=["id"], inplace=True)

# CLEAN target column (THIS IS THE KEY FIX)
df["classification"] = (
    df["classification"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# Map target labels
df["classification"] = df["classification"].map({
    "ckd": 1,
    "notckd": 0
})

# Drop rows where target is missing
df = df.dropna(subset=["classification"])

# Encode categorical features
df.replace({
    "rbc": {"normal": 1, "abnormal": 0},
    "pc": {"normal": 1, "abnormal": 0},
    "pcc": {"present": 1, "notpresent": 0},
    "ba": {"present": 1, "notpresent": 0},
    "htn": {"yes": 1, "no": 0},
    "dm": {"yes": 1, "no": 0},
    "cad": {"yes": 1, "no": 0},
    "appet": {"good": 1, "poor": 0},
    "pe": {"yes": 1, "no": 0},
    "ane": {"yes": 1, "no": 0}
}, inplace=True)

# Convert all columns to numeric
df = df.apply(pd.to_numeric, errors="coerce")

# Fill missing values with column mean
df.fillna(df.mean(), inplace=True)

# Split features and target
X = df.drop(columns=["classification"])
y = df["classification"].astype(int)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open("kidney.pkl", "wb"))

print("✅ Kidney model trained successfully")
