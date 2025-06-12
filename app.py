import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("diabetes_model.joblib")  # Consider renaming the file

# Label encoders
gender_map = {"Male": 0, "Female": 1}
smoking_history_map = {"Never": 0, "Current": 1, "No info": 2}
heart_disease_map = {"No": 0, "Yes": 1}
hypertension_map = {"No": 0, "Yes": 1}
Diabetes_map = {"No": 0, "Yes": 1}

# Streamlit UI
st.title("Stark Health Diabetes Prediction App")

# Numeric inputs
age = st.number_input("Age", min_value=18, max_value=100)
bmi = st.number_input("BMI", min_value=18.5)
HbA1c_level = st.number_input("HbA1c level", min_value=4.0)
blood_glucose_level = st.number_input("Blood glucose level", min_value=70)

# Categorical inputs
gender = st.selectbox("Gender", list(gender_map.keys()))
have_hypertension = st.selectbox("Do you have hypertension?", list(hypertension_map.keys()))
have_heart_disease = st.selectbox("Do you have heart disease?", list(heart_disease_map.keys()))
smoking_history = st.selectbox("Smoking History", list(smoking_history_map.keys()))
have_diabetes = st.selectbox("Do you have diabetes?", list(Diabetes_map.keys()))

# DataFrame
input_data = pd.DataFrame([{
    "Age": age,
    "gender": gender_map[gender],
    "hypertension": hypertension_map[have_hypertension],
    "heart_disease": heart_disease_map[have_heart_disease],
    "smoking_history": smoking_history_map[smoking_history],
    "bmi": bmi,
    "HbA1c_level": HbA1c_level,
    "blood_glucose_level": blood_glucose_level,
    "diabetes": Diabetes_map[have_diabetes],
}])

# Prediction
if st.button("Predict Diabetes"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {'Diabetic (1)' if prediction[0] == 1 else 'Not Diabetic (0)'}")
