import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from PIL import Image

X_test = []
X_inner = []
model = joblib.load(r"./random_forest.joblib")

st.title(f'Lung Cancer Diagnosis - Online Screening Tool')
st.subheader("A Random Forest Classifier based ML Model to screen a patient for cancer based on symptoms given :")
st.text("Created by Anirudh Bharadwaj Vangara")
diagnosis = ""
my_bar = st.progress(0)

genre = st.radio(
    "Are you experiencing Yellow Fingers?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing Coughing?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing Chest Pain?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing Fatigue?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing Wheezing?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing Anxiety?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing a shortness of breath?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing swallowing difficulty?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)

def getDiagnosis():
    X_test.append(X_inner)
    y_pred = model.predict(X_test)
    if y_pred == 0:
        diagnosis = "No Lung Cancer Predicted"
        st.subheader(f"{diagnosis}")
        st.success('Diagnosis Released! ✅')
    else:
        diagnosis = "Lung Cancer Predicted"
        st.subheader(f"{diagnosis}")
        st.success('Diagnosis Released! ✅')


submitBtn = st.button("Get Diagnosis", on_click=getDiagnosis,disabled=False)






# if genre == 'Yes':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn't select comedy.")
