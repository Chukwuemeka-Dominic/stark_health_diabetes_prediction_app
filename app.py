import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("diabetes_model.joblib")  # Make sure this is your final model file

# Define label encoders used during training
gender_map = {"Male": 0, "Female": 1}
smoking_history_map = {"Never": 0, "Current": 1, "No info": 2}
heart_disease_map = {"No": 0, "Yes": 1}
hypertension_map = {"No": 0, "Yes": 1}

# Streamlit UI
st.title("Stark Health - Diabetes Risk Prediction App")

st.markdown("Enter patient details below to predict the risk of developing diabetes.")

# Numeric input fields
age = st.number_input("Age", min_value=18, max_value=100)
bmi = st.number_input("BMI", min_value=10.0)
HbA1c_level = st.number_input("HbA1c level", min_value=4.0)
blood_glucose_level = st.number_input("Blood glucose level", min_value=70.0)

# Categorical input fields
gender = st.selectbox("Gender", list(gender_map.keys()))
have_hypertension = st.selectbox("Do you have hypertension?", list(hypertension_map.keys()))
have_heart_disease = st.selectbox("Do you have heart disease?", list(heart_disease_map.keys()))
smoking_history = st.selectbox("Smoking History", list(smoking_history_map.keys()))

# Prepare input data
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

# Make prediction
if st.button("Predict Diabetes Risk"):
    prediction = model.predict(input_data)
    result = "High Risk of Diabetes (1)" if prediction[0] == 1 else "Low Risk of Diabetes (0)"
    st.success(f"Prediction Result: {result}")
