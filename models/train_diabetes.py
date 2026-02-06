import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('../datasets/diabetes.csv')

# Features and target
X = df[['Pregnancies','Glucose','BloodPressure','SkinThickness',
        'Insulin','BMI','DiabetesPedigreeFunction','Age']]
y = df['Outcome']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
pickle.dump(model, open('diabetes.pkl', 'wb'))

print("Diabetes model trained and saved successfully")
