<h1>🏥 Health-Insight</h1>

<p>End-to-End ML-Powered Disease Prediction Web Application

Health-Insight is a full-stack web application that integrates multiple machine learning models with a Flask backend to provide real-time disease risk predictions. The system is designed with production-style considerations such as feature consistency, model serialization, dynamic form generation, and robust error handling.
</p>
<h2>🚀 Features</h2>

<ul><l>Multi-disease prediction (Diabetes, Heart, Kidney, Liver, Cancer)</l>

<l>Individual ML model per disease</l>

<l>Dynamic input forms based on disease-specific features</l>

<l>Flask REST backend with real-time inference</l>

<l>Model persistence using Pickle</l>

<l>Input validation and categorical encoding</l>

<l>Scalable and modular project structure</l></ul>

<h2>🛠 Tech Stack</h2>
<u>
<l>Backend: Python, Flask</l>

<l>Machine Learning: Scikit-learn, Pandas, NumPy</l>

<l>Models: RandomForestClassifier</l>

<l>Frontend: HTML, CSS, JavaScript</l>

<l>Serialization: Pickle</l>
</u>

<h2>📂 Project Structure</h2>
#Health-Insight/
│
├── app.py
├── models/
│   ├── diabetes.pkl
│   ├── heart.pkl
│   ├── kidney.pkl
│   ├── liver.pkl
│   └── cancer.pkl
│
├── training/
│   ├── diabetes.py
│   ├── heart.py
│   ├── kidney.py
│   ├── liver.py
│   └── cancer.py
│
├── datasets/
│   ├── diabetes.csv
│   ├── heart.csv
│   ├── kidney.csv
│   ├── liver.csv
│   └── cancer.csv
│
├── templates/
│   ├── index.html
│   ├── form.html
│   └── result.html
│
├── static/
│   ├── css/
│   └── js/
│
└── README.md

<h2>⚙️ How It Works</h2>
<ul>
<l>Each disease has a separately trained ML model.</l>

<l>Models are serialized using Pickle.</l>

<l>Flask dynamically loads the correct model and feature set.</l>

<l>User inputs are validated and transformed before prediction.</l>

<l>Predictions are returned in real time via the web interface.</l>
</u>
<h2>▶️ Run Locally</h2>
#pip install -r requirements.txt
#python app.py


#Open http://127.0.0.1:5000/ in your browser.

<h2>🧠 Key Learnings</h2>
<u>
<l>Maintaining feature consistency between training and inference</l>

<l>Handling categorical encoding in production ML systems</l>

<l>Debugging real-world ML deployment issues</l>

<l>Designing modular and scalable backend architecture</l>
</u>
<h2>📌 Future Improvements</h2>

<l>REST API endpoints</l>

<l>Authentication & user history</l>

<l>Model monitoring & retraining pipeline</l>

<l>Dockerized deployment</l>
