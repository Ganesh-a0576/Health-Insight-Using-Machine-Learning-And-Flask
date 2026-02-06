<h1>🏥 Health-Insight using machine learing and flask</h1>

<p>End-to-End ML-Powered Disease Prediction Web Application

Health-Insight is a full-stack web application that integrates multiple machine learning models with a Flask backend to provide real-time disease risk predictions. The system is designed with production-style considerations such as feature consistency, model serialization, dynamic form generation, and robust error handling.
</p>
<h2>🚀 Features</h2>

<ul><l> -Multi-disease prediction (Diabetes, Heart, Kidney, Liver, Cancer)</l>

<l> -Individual ML model per disease</l>

<l> -Dynamic input forms based on disease-specific features</l>

<l> -Flask REST backend with real-time inference</l>

<l> -Model persistence using Pickle</l>

<l> -Input validation and categorical encoding</l>

<l> -Scalable and modular project structure</l></ul>

<h2>🛠 Tech Stack</h2>
<u>
<l> -Backend: Python, Flask</l>

<l> -Machine Learning: Scikit-learn, Pandas, NumPy</l>

<l> -Models: RandomForestClassifier</l>

<l> -Frontend: HTML, CSS, JavaScript</l>

<l> -Serialization: Pickle</l>
</u>

<h2>📂 Project Structure</h2>
``` bash
### Health-Insight/ <br>
│ <br>
├── app.py  <br>
├── models/ <br>
│   ├── diabetes.pkl  <br>
│   ├── heart.pkl   <br>
│   ├── kidney.pkl  <br>
│   ├── liver.pkl   <br>
│   └── cancer.pkl  <br>
│  <br>
├── training/  <br>
│   ├── diabetes.py  <br>
│   ├── heart.py  <br>
│   ├── kidney.py  <br>
│   ├── liver.py  <br>
│   └── cancer.py  <br>
│  <br>
├── datasets/  <br>
│   ├── diabetes.csv  <br>
│   ├── heart.csv  <br>
│   ├── kidney.csv  <br>
│   ├── liver.csv  <br>
│   └── cancer.csv  <br>
│   <br>
├── templates/  <br>
│   ├── index.html  <br>
│   ├── form.html   <br>
│   └── result.html  <br>
│   <br>
├── static/   <br>
│   ├── css/  <br>
│   └── js/   <br>
│  <br>
└── README.md  <br>
<br>
```

<h2>⚙️ How It Works</h2>
<ul>
<l> - Each disease has a separately trained ML model.</l>

<l> - Models are serialized using Pickle.</l>

<l> - Flask dynamically loads the correct model and feature set.</l>

<l> - User inputs are validated and transformed before prediction.</l>

<l> - Predictions are returned in real time via the web interface.</l>
</u>
<h2>▶️ Run Locally</h2>
```bash
pip install -r requirements.txt
python app.py 
```


### Open http://127.0.0.1:5000/ in your browser.

<h2>🧠 Key Learnings</h2>
<u>
- <l>Maintaining feature consistency between training and inference</l>

- <l>Handling categorical encoding in production ML systems</l>

- <l>Debugging real-world ML deployment issues</l>

- <l>Designing modular and scalable backend architecture</l>
</u>
<h2>📌 Future Improvements</h2>

- <l>REST API endpoints</l>

- <l>Authentication & user history</l>

- <l>Model monitoring & retraining pipeline</l>

- <l>Dockerized deployment</l>
