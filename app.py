from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained models
MODELS = {
    "diabetes": pickle.load(open("models/diabetes.pkl", "rb")),
    "cancer": pickle.load(open("models/cancer.pkl", "rb")),
    "heart": pickle.load(open("models/heart.pkl", "rb")),
    "kidney": pickle.load(open("models/kidney.pkl", "rb")),
    "liver": pickle.load(open("models/liver.pkl", "rb")),
}

# Feature mapping (INPUT ONLY — NO TARGETS)
FEATURES = {
    "diabetes": [
        "Pregnancies","Glucose","BloodPressure","SkinThickness",
        "Insulin","BMI","DiabetesPedigreeFunction","Age"
    ],

    "heart": [
        "age","sex","cp","trestbps","chol","fbs",
        "restecg","thalach","exang","oldpeak","slope","ca","thal","target"
    ],

    "kidney": [
        "age","bp","sg","al","su","rbc","pc","pcc","ba",
        "bgr","bu","sc","sod","pot","hemo","pcv","wc","rc",
        "htn","dm","cad","appet","pe","ane"
    ],

    "cancer": [
        "radius_mean","texture_mean","perimeter_mean","area_mean",
        "smoothness_mean","compactness_mean","concavity_mean",
        "concave points_mean","symmetry_mean","fractal_dimension_mean",
        "radius_se","texture_se","perimeter_se","area_se",
        "smoothness_se","compactness_se","concavity_se",
        "concave points_se","symmetry_se","fractal_dimension_se",
        "radius_worst","texture_worst","perimeter_worst","area_worst",
        "smoothness_worst","compactness_worst","concavity_worst",
        "concave points_worst","symmetry_worst","fractal_dimension_worst"
    ],

    "liver": [
        "Age","Gender","Total_Bilirubin","Direct_Bilirubin",
        "Alkaline_Phosphotase","Alamine_Aminotransferase",
        "Aspartate_Aminotransferase","Total_Protiens",
        "Albumin","Albumin_and_Globulin_Ratio"
    ]
}

# -------- PREPROCESSING (CRITICAL) --------
def preprocess_input(disease, form):
    data = []

    for field in FEATURES[disease]:
        value = form[field]

        # Liver categorical
        if disease == "liver" and field == "Gender":
            value = 1 if value.lower() == "male" else 0

        # Kidney categoricals
        if disease == "kidney":
            maps = {
                "yes": 1, "no": 0,
                "normal": 1, "abnormal": 0,
                "present": 1, "notpresent": 0,
                "good": 1, "poor": 0
            }
            value = maps.get(value.lower(), value)

        data.append(float(value))

    return np.array(data).reshape(1, -1)

# -------- ROUTES --------
@app.route('/')
def index():
    return render_template("index.html", diseases=FEATURES.keys())

@app.route('/form/<disease>')
def form(disease):
    return render_template("form.html",
                           disease=disease,
                           fields=FEATURES[disease])

@app.route('/predict/<disease>', methods=['POST'])
def predict(disease):
    input_data = preprocess_input(disease, request.form)
    prediction = MODELS[disease].predict(input_data)[0]

    return render_template("result.html",
                           disease=disease,
                           prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
