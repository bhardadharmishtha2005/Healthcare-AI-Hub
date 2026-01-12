# Smart Health AI Assistant

A lightweight, high-performance healthcare diagnostic hub built with **Python**. This project demonstrates the integration of Machine Learning and Natural Language Processing in a single web interface.

# Key Features
Diabetes Risk Predictor (ML): Utilizes a Random Forest Classifier to analyze patient metrics like Glucose levels, BMI, and Age to predict health risks instantly.

Symptom Urgency Analyzer (NLP): Leverages TextBlob for sentiment analysis on patient-described symptoms, allowing for automated triage based on the distress level found in the text.

Interactive UI: A responsive dashboard built with Streamlit, featuring real-time data input and side-bar navigation for a seamless user experience.

# Tech Stack & Tools
Frontend: Streamlit for a responsive and interactive web interface.

Machine Learning: Scikit-learn for predictive modeling and data classification.

NLP: TextBlob for natural language processing and emotional tone detection.

Data Handling: Pandas and NumPy for high-speed data manipulation and synthetic dataset generation.

Development Environment: VS Code on Microsoft Windows.

## How to Run Locally
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run healthcare.py`
