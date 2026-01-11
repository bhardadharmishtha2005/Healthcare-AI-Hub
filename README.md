# Smart Health AI Assistant

A lightweight, high-performance healthcare diagnostic hub built with **Python**. This project demonstrates the integration of Machine Learning and Natural Language Processing in a single web interface.

## Key Features
- **Diabetes Risk Prediction:** A **Random Forest Classifier** trained to predict health risks based on Glucose, BMI, and Age.
- **Symptom Urgency Analyzer:** Uses **NLP (TextBlob)** to perform sentiment analysis on patient descriptions, identifying high-distress cases for immediate attention.

## Tech Stack
- **Web App:** Streamlit
- **Machine Learning:** Scikit-learn
- **NLP:** TextBlob
- **Data Handling:** Pandas, NumPy

## 🏃 How to Run Locally
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run healthcare.py`