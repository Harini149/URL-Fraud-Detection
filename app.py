import streamlit as st
import joblib
import numpy as np
from utils.feature_extraction import extract_features

# Load model
model = joblib.load("models/url_fraud_rf_model.pkl")

# UI Title
st.set_page_config(page_title="URL Fraud Detection", layout="centered")
st.title("🔐 URL Fraud Detection System")
st.write("Check whether a website URL is **Safe or Malicious**")

# Input
url = st.text_input("Enter Website URL")

# Predict
if st.button("Analyze URL"):
    if url.strip() == "":
        st.warning("Please enter a valid URL")
    else:
        features = np.array(extract_features(url)).reshape(1, -1)

        prob = model.predict_proba(features)[0]

        safe = round(prob[0] * 100, 2)
        malicious = round(prob[1] * 100, 2)

        if malicious > safe:
            st.error(f"🚨 Malicious URL Detected ({malicious}%)")
        else:
            st.success(f"✅ Safe URL ({safe}%)")

        st.info(f"Safe Probability: {safe}%\nMalicious Probability: {malicious}%")
