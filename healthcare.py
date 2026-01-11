import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from textblob import TextBlob

# --- 1. DATA & MODEL ---
def train_model():
    # Synthetic data: [Glucose, BMI, Age]
    X = [[85, 18, 20], [160, 32, 45], [190, 35, 55], [90, 21, 25], [175, 33, 62], [115, 25, 30]]
    y = [0, 1, 1, 0, 1, 0] # 0 = Healthy, 1 = Risk
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)
    return model

model = train_model()

# --- 2. STREAMLIT UI ---
st.set_page_config(page_title="AI Health Hub")
st.title("🏥 Smart Health AI Assistant")
st.write("A lightweight AI project using Python, ML, and NLP")

tab1, tab2 = st.tabs(["Disease Predictor (ML)", "Symptom Analyzer (NLP)"])

with tab1:
    st.header("Diabetes Risk Prediction")
    glu = st.number_input("Glucose Level", value=100)
    bmi = st.number_input("BMI", value=22)
    age = st.number_input("Age", value=25)
    
    if st.button("Analyze Results"):
        prediction = model.predict([[glu, bmi, age]])
        if prediction[0] == 1:
            st.error("Result: High Risk Detected")
        else:
            st.success("Result: Low Risk / Healthy")

with tab2:
    st.header("Symptom Urgency Check")
    user_input = st.text_area("Describe your symptoms (e.g., 'I feel a bit tired' or 'I HAVE SEVERE CHEST PAIN')")
    
    if st.button("Check Urgency"):
        if user_input:
            blob = TextBlob(user_input)
            # Sentiment polarity < -0.3 usually means high distress
            if blob.sentiment.polarity < -0.3:
                st.warning("🚨 Alert: This sounds urgent. Please seek medical attention.")
            else:
                st.info("✅ Routine: Symptoms seem mild. Monitor and rest.")

st.sidebar.write("### Tech Stack")
st.sidebar.write("- Python\n- Scikit-learn (ML)\n- TextBlob (NLP)\n- Streamlit (UI)")