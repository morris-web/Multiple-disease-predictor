# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:12:31 2024


@author: Morris
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Load the saved models
diabetes_model = pickle.load(open('C:/Users/MORIS/Desktop/Multiple Disease Prediction System/Saved Model/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/MORIS/Desktop/Multiple Disease Prediction System/Saved Model/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/MORIS/Desktop/Multiple Disease Prediction System/Saved Model/parkinsons_model.sav', 'rb'))
breast_cancer_model = pickle.load(open('C:/Users/MORIS/Desktop/Multiple Disease Prediction System/Saved Model/breast_cancer_model.sav', 'rb'))


# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Prediction System',
                       ['Diabetes Prediction',
                        'Heart Disease Prediction',
                        'Parkinsons Prediction', 
                        'Breast Cancer Prediction'],
                       icons=['activity', 'heart', 'person', 'bandaid'],
                       default_index=0)


# Function to validate inputs
def validate_input(value, value_type):
    try:
        if value_type == "float":
            return float(value)
        elif value_type == "int":
            return int(value)
    except ValueError:
        return None

# Set a background image and custom CSS styles
st.markdown(
    """
    <style>
    body {
        background-image: url('https://www.linkpicture.com/q/health_background.jpg');
        background-size: cover;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        margin-top: 20px;
    }
    .stNumberInput > div > div > input {
        border: 2px solid #4CAF50;
        padding: 5px;
        border-radius: 10px;
        font-size: 16px;
    }
    .stMarkdown {
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Diabetes prediction page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')
    
    # Input fields using a form
    with st.form(key='diabetes_form'):
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)
        Glucose = st.number_input('Glucose Level', min_value=0.0, step=0.1)
        BloodPressure = st.number_input('Blood Pressure Value', min_value=0.0, step=0.1)
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0.0, step=0.1)
        Insulin = st.number_input('Insulin Level', min_value=0.0, step=0.1)
        BMI = st.number_input('BMI Value', min_value=0.0, step=0.1)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value=0.0, step=0.1)
        Age = st.number_input('Age', min_value=0, step=1)
        submit_button = st.form_submit_button('Diabetes Test Result')
    
    # Code for prediction
    if submit_button:
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([input_data])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'

        # Show result in an expander (simulated popup)
        with st.expander("Diabetes Test Result"):
            st.markdown(f"**{diab_diagnosis}**")

# Heart disease prediction page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    # Input fields using a form
    with st.form(key='heart_disease_form'):
        age = st.number_input('Age', min_value=0, step=1)
        sex = st.selectbox('Sex', ['Male', 'Female'])
        cp = st.number_input('Chest Pain Type', min_value=0, step=1)
        trestbps = st.number_input('Resting Blood Pressure Value', min_value=0.0, step=0.1)
        chol = st.number_input('Serum Cholesterol', min_value=0.0, step=0.1)
        fbs = st.number_input('Fasting Blood Sugar', min_value=0.0, step=0.1)
        restecg = st.number_input('Resting Electrocardiographic Value', min_value=0, step=1)
        thalach = st.number_input('Max Heart Rate Achieved', min_value=0.0, step=0.1)
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
        oldpeak = st.number_input('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, step=0.1)
        slope = st.number_input('Slope of the Peak Exercise ST Segment', min_value=0, step=1)
        ca = st.number_input('Number of Major Vessels', min_value=0, step=1)
        thal = st.number_input('Thalassemia', min_value=0, step=1)
        submit_button = st.form_submit_button('Heart Disease Test Result')
    
    # Code for prediction
    if submit_button:
        sex = 1 if sex == 'Male' else 0
        exang = 1 if exang == 'Yes' else 0
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        heart_prediction = heart_disease_model.predict([input_data])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'

        # Show result in an expander (simulated popup)
        with st.expander("Heart Disease Test Result"):
            st.markdown(f"**{heart_diagnosis}**")

# Parkinson's prediction page
if selected == 'Parkinsons Prediction':
    # Page title
    st.title('Parkinsons Prediction using ML')
    
    # Input fields using a form
    with st.form(key='parkinsons_form'):
        fo = st.number_input('MDVP: Fo (Hz)', min_value=0.0, step=0.1)
        fhi = st.number_input('MDVP: Fhi (Hz)', min_value=0.0, step=0.1)
        flo = st.number_input('MDVP: Flo (Hz)', min_value=0.0, step=0.1)
        jitter_percent = st.number_input('MDVP: Jitter (%)', min_value=0.0, step=0.1)
        jitter_abs = st.number_input('MDVP: Jitter (Abs)', min_value=0.0, step=0.1)
        rap = st.number_input('MDVP: RAP', min_value=0.0, step=0.1)
        ppq = st.number_input('MDVP: PPQ', min_value=0.0, step=0.1)
        ddp = st.number_input('Jitter: DDP', min_value=0.0, step=0.1)
        shimmer = st.number_input('MDVP: Shimmer', min_value=0.0, step=0.1)
        shimmer_db = st.number_input('MDVP: Shimmer (dB)', min_value=0.0, step=0.1)
        apq3 = st.number_input('Shimmer: APQ3', min_value=0.0, step=0.1)
        apq5 = st.number_input('Shimmer: APQ5', min_value=0.0, step=0.1)
        apq = st.number_input('MDVP: APQ', min_value=0.0, step=0.1)
        dda = st.number_input('Shimmer: DDA', min_value=0.0, step=0.1)
        nhr = st.number_input('NHR', min_value=0.0, step=0.1)
        hnr = st.number_input('HNR', min_value=0.0, step=0.1)
        rpde = st.number_input('RPDE', min_value=0.0, step=0.1)
        dfa = st.number_input('DFA', min_value=0.0, step=0.1)
        spread1 = st.number_input('Spread1', min_value=0.0, step=0.1)
        spread2 = st.number_input('Spread2', min_value=0.0, step=0.1)
        d2 = st.number_input('D2', min_value=0.0, step=0.1)

# Breast cancer prediction page
if selected == 'Breast Cancer Prediction':
    # Page title
    st.title('Breast Cancer Prediction using ML')
    
    # Input fields using a form
    with st.form(key='breast_cancer_form'):
        mean_radius = st.number_input('Mean Radius', min_value=0.0, step=0.1)
        mean_texture = st.number_input('Mean Texture', min_value=0.0, step=0.1)
        mean_perimeter = st.number_input('Mean Perimeter', min_value=0.0, step=0.1)
        mean_area = st.number_input('Mean Area', min_value=0.0, step=0.1)
        mean_smoothness = st.number_input('Mean Smoothness', min_value=0.0, step=0.1)
        mean_compactness = st.number_input('Mean Compactness', min_value=0.0, step=0.1)
        mean_concavity = st.number_input('Mean Concavity', min_value=0.0, step=0.1)
        mean_concave_points = st.number_input('Mean Concave Points', min_value=0.0, step=0.1)
        mean_symmetry = st.number_input('Mean Symmetry', min_value=0.0, step=0.1)
        mean_fractal_dimension = st.number_input('Mean Fractal Dimension', min_value=0.0, step=0.1)
        radius_error = st.number_input('Radius Error', min_value=0.0, step=0.1)
        texture_error = st.number_input('Texture Error', min_value=0.0, step=0.1)
        perimeter_error = st.number_input('Perimeter Error', min_value=0.0, step=0.1)
        area_error = st.number_input('Area Error', min_value=0.0, step=0.1)
        smoothness_error = st.number_input('Smoothness Error', min_value=0.0, step=0.1)
        compactness_error = st.number_input('Compactness Error', min_value=0.0, step=0.1)
        concavity_error = st.number_input('Concavity Error', min_value=0.0, step=0.1)
        concave_points_error = st.number_input('Concave Points Error', min_value=0.0, step=0.1)
        symmetry_error = st.number_input('Symmetry Error', min_value=0.0, step=0.1)
        fractal_dimension_error = st.number_input('Fractal Dimension Error', min_value=0.0, step=0.1)
        worst_radius = st.number_input('Worst Radius', min_value=0.0, step=0.1)
        worst_texture = st.number_input('Worst Texture', min_value=0.0, step=0.1)
        worst_perimeter = st.number_input('Worst Perimeter', min_value=0.0, step=0.1)
        worst_area = st.number_input('Worst Area', min_value=0.0, step=0.1)
        worst_smoothness = st.number_input('Worst Smoothness', min_value=0.0, step=0.1)
        worst_compactness = st.number_input('Worst Compactness', min_value=0.0, step=0.1)
        worst_concavity = st.number_input('Worst Concavity', min_value=0.0, step=0.1)
        worst_concave_points = st.number_input('Worst Concave Points', min_value=0.0, step=0.1)
        worst_symmetry = st.number_input('Worst Symmetry', min_value=0.0, step=0.1)
        worst_fractal_dimension = st.number_input('Worst Fractal Dimension', min_value=0.0, step=0.1)
        submit_button = st.form_submit_button('Breast Cancer Test Result')

# Code for prediction
if submit_button:
    input_data = [
        mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness,
        mean_compactness, mean_concavity, mean_concave_points, mean_symmetry,
        mean_fractal_dimension, radius_error, texture_error, perimeter_error,
        area_error, smoothness_error, compactness_error, concavity_error,
        concave_points_error, symmetry_error, fractal_dimension_error,
        worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness,
        worst_compactness, worst_concavity, worst_concave_points, worst_symmetry,
        worst_fractal_dimension
    ]
    breast_cancer_prediction = breast_cancer_model.predict([input_data])
    cancer_diagnosis = 'The tumor is malignant' if breast_cancer_prediction[0] == 1 else 'The tumor is benign'

    # Show result in an expander (simulated popup)
    with st.expander("Breast Cancer Test Result"):
        st.markdown(f"**{cancer_diagnosis}**")


