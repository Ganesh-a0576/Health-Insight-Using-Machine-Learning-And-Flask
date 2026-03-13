# 🏥 Health-Insight — ML-Powered Disease Prediction

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Array-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)

**An end-to-end ML-powered web application that predicts risk for multiple diseases in real time.**

[Live Demo](#) · [Report Bug](../../issues) · [Request Feature](../../issues)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Supported Diseases](#-supported-diseases)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Model Performance](#-model-performance)
- [Key Learnings](#-key-learnings)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 📖 About the Project

**Health-Insight** is a full-stack web application that integrates multiple machine learning models with a Flask backend to deliver real-time disease risk predictions directly in the browser.

Designed with production-style considerations in mind, this project addresses challenges like **feature consistency between training and inference**, **model serialization**, **dynamic form generation**, and **robust error handling** — making it more than just a demo, but a template for real-world ML deployment.

> ⚠️ **Disclaimer:** This application is intended for educational and research purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

---

## 🦠 Supported Diseases

| Disease           | Model File       | Dataset         |
|-------------------|-----------------|-----------------|
| 🩸 Diabetes       | `diabetes.pkl`  | `diabetes.csv`  |
| ❤️ Heart Disease  | `heart.pkl`     | `heart.csv`     |
| 🫘 Kidney Disease | `kidney.pkl`    | `kidney.csv`    |
| 🫀 Liver Disease  | `liver.pkl`     | `liver.csv`     |
| 🔬 Cancer         | `cancer.pkl`    | `cancer.csv`    |

---

## ✨ Features

- 🤖 **Individual ML model per disease** — each condition has its own dedicated RandomForestClassifier
- 📋 **Dynamic input forms** — automatically generated based on disease-specific feature sets
- ⚡ **Real-time predictions** — instant inference via Flask REST backend
- 💾 **Model persistence** — serialized and loaded using Pickle for fast startup
- ✅ **Input validation** — client and server-side checks before inference
- 🔡 **Categorical encoding** — handles mixed data types in production
- 🧱 **Modular architecture** — clean separation of training, inference, and UI layers
- 📱 **Responsive UI** — works across desktop and mobile browsers

---

## 🛠 Tech Stack

| Layer             | Technology                            |
|-------------------|---------------------------------------|
| **Backend**       | Python 3.x, Flask                     |
| **ML Framework**  | Scikit-learn (RandomForestClassifier) |
| **Data Handling** | Pandas, NumPy                         |
| **Serialization** | Pickle                                |
| **Frontend**      | HTML5, CSS3, JavaScript               |
| **Templating**    | Jinja2                                |

---

## ⚙️ How It Works

```
User selects a disease
        │
        ▼
Dynamic form rendered with disease-specific input fields
        │
        ▼
User submits health parameters
        │
        ▼
Flask validates & encodes inputs
        │
        ▼
Correct .pkl model loaded for the selected disease
        │
        ▼
RandomForestClassifier runs inference
        │
        ▼
Prediction result displayed on result.html
```

1. **Training Phase** — Each disease has a standalone training script (`training/<disease>.py`) that preprocesses the dataset, trains a `RandomForestClassifier`, and saves the model as a `.pkl` file.
2. **Inference Phase** — When a user submits a form, Flask loads the corresponding `.pkl` model, applies the same preprocessing pipeline, and returns the prediction.
3. **Feature Consistency** — Feature names and encoding schemes are kept consistent between training and inference to prevent silent prediction errors.

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed on your system:

- **Python 3.x** — [Download](https://www.python.org/downloads/)
- **pip** — comes with Python
- **Git** — [Download](https://git-scm.com/)

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/Health-Insight.git
cd Health-Insight
```

2. **Create and activate a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

3. **Install all dependencies:**

```bash
pip install -r requirements.txt
```

4. **(Optional) Retrain the models:**

```bash
python training/diabetes.py
python training/heart.py
python training/kidney.py
python training/liver.py
python training/cancer.py
```

> Pre-trained `.pkl` files are included in the `models/` directory so retraining is optional.

---

## 💻 Usage

1. **Start the Flask development server:**

```bash
python app.py
```

2. **Open your browser and visit:**

```
http://127.0.0.1:5000/
```

3. **Select a disease**, fill in the health parameters, and click **Predict** to receive your risk assessment instantly.

---

## 📁 Project Structure

```
Health-Insight/
│
├── app.py                    # Main Flask app — routes & inference logic
├── requirements.txt          # All Python dependencies
│
├── models/                   # Serialized trained ML models
│   ├── diabetes.pkl
│   ├── heart.pkl
│   ├── kidney.pkl
│   ├── liver.pkl
│   └── cancer.pkl
│
├── training/                 # Standalone training scripts per disease
│   ├── diabetes.py
│   ├── heart.py
│   ├── kidney.py
│   ├── liver.py
│   └── cancer.py
│
├── datasets/                 # Raw CSV datasets used for training
│   ├── diabetes.csv
│   ├── heart.csv
│   ├── kidney.csv
│   ├── liver.csv
│   └── cancer.csv
│
├── templates/                # Jinja2 HTML templates
│   ├── index.html            # Landing page — disease selector
│   ├── form.html             # Dynamic input form
│   └── result.html           # Prediction result display
│
├── static/                   # Static assets
│   ├── css/                  # Stylesheets
│   └── js/                   # JavaScript files
│
└── README.md
```

---

## 🔌 API Endpoints

| Method | Endpoint             | Description                             |
|--------|----------------------|-----------------------------------------|
| GET    | `/`                  | Home page — disease selection           |
| GET    | `/predict/<disease>` | Load input form for selected disease    |
| POST   | `/predict/<disease>` | Submit form and return prediction result|

**Example POST body** for diabetes prediction:

```json
{
  "pregnancies": 2,
  "glucose": 138,
  "blood_pressure": 62,
  "skin_thickness": 35,
  "insulin": 0,
  "bmi": 33.6,
  "diabetes_pedigree": 0.627,
  "age": 47
}
```

---

## 📊 Model Performance

> Results from training on the provided datasets. Metrics may vary with different train/test splits.

| Disease        | Algorithm              | Accuracy   |
|----------------|------------------------|------------|
| Diabetes       | RandomForestClassifier | ~76–80%    |
| Heart Disease  | RandomForestClassifier | ~82–86%    |
| Kidney Disease | RandomForestClassifier | ~96–99%    |
| Liver Disease  | RandomForestClassifier | ~72–76%    |
| Cancer         | RandomForestClassifier | ~94–97%    |

---

## 🧠 Key Learnings

- **Feature consistency** — Ensuring training feature names/order exactly match inference inputs to prevent silent errors
- **Categorical encoding in production** — Handling label encoding and one-hot encoding at inference time without refitting
- **Real-world ML deployment** — Debugging shape mismatches, missing values, and dtype inconsistencies
- **Modular backend design** — Separating training logic from inference for clean, maintainable code
- **Flask routing patterns** — Building dynamic, parameterized routes for multi-model applications

---

## 🔮 Future Improvements

- [ ] REST API endpoints with JSON responses for mobile/external integration
- [ ] User authentication and prediction history dashboard
- [ ] Model monitoring, drift detection & automated retraining pipeline
- [ ] Dockerized deployment with `docker-compose`
- [ ] SHAP-based explainability — show which features drove the prediction
- [ ] Confidence scores alongside binary predictions
- [ ] CI/CD pipeline with GitHub Actions

---

## 🤝 Contributing

Contributions are welcome and appreciated!

1. **Fork** the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a **Pull Request**

Please follow [PEP 8](https://peps.python.org/pep-0008/) coding standards and include docstrings for any new functions.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 📬 Contact

**Your Name** — [ganesh1a0576@gmail.com](mailto:ganesh1a0576@gmail.com)

GitHub: [Ganesh-a0576](https://github.com/Ganesh-a0576)

Project Link: [https://github.com/your-username/Health-Insight](https://github.com/Ganesh-a0576/Health-Insight-Using-Machine-Learning-And-Flask)

---

<div align="center">

⭐ If this project helped you, please consider giving it a star — it means a lot!

<br/>

Made with ❤️ and Python

</div>
