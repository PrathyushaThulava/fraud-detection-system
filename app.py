import streamlit as st
import numpy as np
import pickle
import os

# Load model and scaler
model = pickle.load(open("fraud_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# --- Page Configuration ---
st.set_page_config(page_title="Fraud Detection System", page_icon="🛡️", layout="wide")

# --- Sidebar Branding ---
with st.sidebar:
    st.image("fraud_icon.png", width=100)
    st.title("🧠 AI Fraud Detector")
    st.caption("Predict fraudulent transactions using ML")

# --- Main Heading ---
st.markdown("<h1 style='text-align: center; color: #3b8f8f;'>Fraud Detection System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the 30 features below to predict whether a transaction is fraudulent or not.</p>", unsafe_allow_html=True)
st.write("")

# --- Input Form ---
st.subheader("🔍 Input Transaction Features")
input_data = []
cols = st.columns(3)

for i in range(30):
    with cols[i % 3]:
        val = st.number_input(f"Feature {i+1}", min_value=-10000.0, max_value=10000.0, value=0.0, step=0.01)
        input_data.append(val)

# --- Prediction ---
if st.button("🧪 Predict"):
    scaled_input = scaler.transform([input_data])
    prediction = model.predict(scaled_input)

    st.write("## Prediction Result:")
    if prediction[0] == 1:
        st.error("🚨 Fraud Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")
