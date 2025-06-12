# 🩺 Stark Health Diabetes Prediction App

## 🔍 Problem Statement

Diabetes poses significant health risks to Stark Health’s patients and creates additional financial challenges for the clinic. Unfortunately, current methods for early detection at Stark Health lack the precision needed to catch many cases in time, leading to missed opportunities for timely and life-saving interventions.

## 💡 Solution

This **Diabetes Prediction App**, built with **Streamlit** and powered by a machine learning model, helps Stark Health quickly assess a patient's likelihood of having diabetes using routine health indicators such as:

- Age  
- BMI  
- HbA1c Level  
- Blood Glucose Level  
- Smoking History  
- Hypertension & Heart Disease Status  
- Gender  

The model was trained on a real-world health dataset, addressing class imbalance using SMOTE and improving predictive accuracy through scaling and model tuning. Among all models tested, **XGBoost** showed the best performance with **98% accuracy** and **96% recall for diabetic cases**.

## ✅ Features

- Easy-to-use web interface for clinical staff  
- Instant diabetes risk prediction  
- Based on robust machine learning algorithms  
- Supports data-driven decision making at point of care

## 🛠️ Technologies Used

- Python (Pandas, Scikit-learn, XGBoost)  
- Streamlit for the web app interface  
- SMOTE and StandardScaler for data preprocessing  
- Joblib for model saving/loading

## 🚀 How to Run

1. Clone the repository or download the app files  
2. Make sure `diabetes_model.joblib` is in the same folder as the app  
3. Run the app using:

```bash
streamlit run app.py
```

## 📈 Outcome

By implementing this app, Stark Health can improve early detection of diabetes, leading to:

- More targeted patient care  
- Reduced long-term treatment costs  
- Improved clinical outcomes
