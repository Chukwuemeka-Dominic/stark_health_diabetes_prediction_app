import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("diabetes_model.joblib")  # Ensure it's the correct model file

# Define label encoders
gender_map = {"Male": 0, "Female": 1}
smoking_history_map = {"Never": 0, "Current": 1, "No info": 2}
heart_disease_map = {"No": 0, "Yes": 1}
hypertension_map = {"No": 0, "Yes": 1}

# Streamlit UI
st.title("🔬 Stark Health - Diabetes Risk Prediction")

st.markdown("Fill in the patient details below to assess their risk of developing diabetes.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100)
bmi = st.number_input("BMI", min_value=10.0)
HbA1c_level = st.number_input("HbA1c Level", min_value=4.0)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=70.0)

gender = st.selectbox("Gender", list(gender_map.keys()))
have_hypertension = st.selectbox("Do you have hypertension?", list(hypertension_map.keys()))
have_heart_disease = st.selectbox("Do you have heart disease?", list(heart_disease_map.keys()))
smoking_history = st.selectbox("Smoking History", list(smoking_history_map.keys()))

# Prepare the data for prediction
input_data = pd.DataFrame([{
    "Age": age,
    "gender": gender_map[gender],
    "hypertension": hypertension_map[have_hypertension],
    "heart_disease": heart_disease_map[have_heart_disease],
    "smoking_history": smoking_history_map[smoking_history],
    "bmi": bmi,
    "HbA1c_level": HbA1c_level,
    "blood_glucose_level": blood_glucose_level
}])

# Predict button
if st.button("🔍 Predict Diabetes Risk"):
    probability = model.predict_proba(input_data)[0][1]  # Probability of class '1' (diabetic)
    
    if probability < 0.4:
        risk_level = "🟢 Low Risk"
        st.success(f"Prediction: {risk_level} ({probability:.2%} chance of diabetes)")
    elif 0.4 <= probability < 0.7:
        risk_level = "🟡 Medium Risk"
        st.warning(f"Prediction: {risk_level} ({probability:.2%} chance of diabetes)")
    else:
        risk_level = "🔴 High Risk"
        st.error(f"Prediction: {risk_level} ({probability:.2%} chance of diabetes)")
