import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("../datasets/cancer.csv")

# Encode target column
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Drop ID column
df.drop(columns=['id'], inplace=True)

# Features & target
X = df.drop(columns=['diagnosis'])
y = df['diagnosis']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open("cancer.pkl", "wb"))

print("Cancer model trained successfully")
