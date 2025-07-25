\# 🚨 Fraud Detection System for Financial Transactions



A machine learning-powered web app that detects fraudulent financial transactions in real-time. This system uses Logistic Regression and SMOTE to handle class imbalance, with a professional UI built using Streamlit.



!\[Banner](https://cdn-icons-png.flaticon.com/512/2814/2814628.png)



---



\## 🔍 Features



\- 🧠 Predicts fraud using 30 transaction features

\- ⚖️ Handles class imbalance with \*\*SMOTE\*\*

\- ⚙️ Logistic Regression-based ML model

\- 📈 Visualizes fraud vs non-fraud transactions

\- 🧮 Scales features with StandardScaler

\- 🌐 Interactive web UI via Streamlit



---



\## 📁 Project Structure



```



fraud\\\_detection\\\_project/

├── app.py               # Streamlit web app

├── fraud\\\_model.pkl      # Trained logistic regression model

├── scaler.pkl           # Feature scaler (StandardScaler)

├── creditcard.csv       # Dataset used for model and pie chart

├── save\\\_model.py        # Script to train and save model

├── requirements.txt     # All project dependencies

└── README.md            # Project documentation



````



---



\## 📊 Dataset Used



\- \*\*Source\*\*: \[Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

\- 284,807 transactions with 492 frauds (0.17%)

\- Features: `V1` to `V28`, `Amount`, `Time`, and `Class`



---



\## ⚙️ Setup Instructions



\### 🔧 1. Clone Repository



```bash

git clone https://github.com/yourusername/fraud-detection-system.git

cd fraud-detection-system

````



\### 📦 2. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 🚀 3. Launch the App



```bash

streamlit run app.py

```



---



\## 🧠 Model Details



\* \*\*Algorithm\*\*: Logistic Regression

\* \*\*Scaler\*\*: StandardScaler

\* \*\*Imbalance Handling\*\*: SMOTE

\* \*\*Metrics\*\*: 99% accuracy (on balanced dataset)



---



\## 📸 UI Preview



| Form Input (30 Features)                  | Prediction Output                          |

| ----------------------------------------- | ------------------------------------------ |

| !\[Input](https://i.imgur.com/GGkm6eS.png) | !\[Output](https://i.imgur.com/ZQ3rUuw.png) |



---



\## ✅ Requirements



Contents of `requirements.txt`:



```

streamlit

scikit-learn

pandas

numpy

matplotlib

Pillow

```



Install all at once:



```bash

pip install -r requirements.txt

```



---



\## ✨ Author



\*\*Thulava Prathyusha\*\*

B.Tech CSE (AI) | KIIT University

🔗 GitHub: \[yourusername](https://github.com/yourusername)

📧 Email: \[your.email@example.com](mailto:your.email@example.com)



---



\## 🌐 Optional Deployment



You can deploy the app to:



\* \[Streamlit Cloud](https://streamlit.io/cloud)

\* \[Render](https://render.com/)

\* \[Heroku](https://heroku.com/)



Need help deploying? I can help set it up.



---



\## 📝 License



MIT License – feel free to use and modify this project for learning or development.



