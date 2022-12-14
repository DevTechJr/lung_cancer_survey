import streamlit as st
import pandas as pd
import numpy as np
# import sns as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


data = pd.read_csv(r'lungData.csv')
data_new = data.drop(['GENDER', 'AGE', 'PEER_PRESSURE'], axis=1)
symptoms = ['YELLOW_FINGERS', 'ANXIETY', 'FATIGUE ', 'WHEEZING', 'COUGHING', 'SHORTNESS OF BREATH',
            'SWALLOWING DIFFICULTY', 'CHEST PAIN', 'SMOKING', 'ALCOHOL CONSUMING', 'CHRONIC DISEASE', 'ALLERGY ']
X = data_new[symptoms]
y = data_new.LUNG_CANCER

X_train, X_test, y_train, y_test = train_test_split( X, y)

le = LabelEncoder()
y_train= le.fit_transform(y_train)
y_test= le.transform(y_test)

key = {2: 'YES', 1: 'NO'}
# for sys in symptoms:
# 	sns.countplot(x = X_train[sys].replace(key))

model =RandomForestClassifier()
model.fit(X_train, y_train)

X_test = []
X_inner = []


st.title(f'Lung Cancer Prediction - Online Screening Tool')
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
    "Are you experiencing Anxiety?",
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
    "Are you experiencing Coughing?",
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
genre = st.radio(
    "Are you experiencing Chest Pain?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Do you Smoke?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Do you consume Alcohol?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Do you suffer from any Chronic Disease?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Do you suffer from any Allergies?",
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
        st.success('Prediction Released! ✅')
    else:
        diagnosis = "Lung Cancer Predicted"
        st.subheader(f"{diagnosis}")
        st.success('Prediction Released! ✅')


submitBtn = st.button("Get Diagnosis", on_click=getDiagnosis,disabled=False)






# if genre == 'Yes':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn't select comedy.")
