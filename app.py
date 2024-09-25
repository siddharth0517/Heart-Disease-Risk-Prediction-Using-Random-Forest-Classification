import streamlit as st
import numpy as np
import pickle

# Load the trained model and scaler
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Streamlit app
st.title("Heart Disease Risk Prediction")
st.write("This app predicts the risk of heart disease based on several input features.")

# Input features
age = st.number_input('Age', min_value=1, max_value=120, value=25, step=1)
sex = st.selectbox('Gender', ['Male', 'Female'])
trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=200, value=120)
chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=100, max_value=400, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['True', 'False'])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])

# Encoding categorical variables
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'True' else 0
exang = 1 if exang == 'Yes' else 0

# Create feature array
features = np.array([[age, sex, trestbps, chol, fbs, thalach, exang]])

if st.button('Predict'):
    prediction = model.predict(features)
    result = 'High Risk of Heart Disease' if prediction[0] == 1 else 'Low Risk of Heart Disease'
    st.subheader(f"Prediction: {result}")

# Enhance the appearance of the app
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("### About")
st.write("This app uses a Random Forest Classifier to predict the risk of heart disease. Enter the required details above and hit 'Predict' to see the result.")
