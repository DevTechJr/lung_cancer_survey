import streamlit as st
import pandas as pd
import numpy as np
# import sns as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score


data = pd.read_csv(r'lungData.csv')
data_new = data.drop(['GENDER'], axis=1)
symptoms = ['AGE','SMOKING','YELLOW_FINGERS', 'ANXIETY','PEER_PRESSURE','CHRONIC DISEASE', 'FATIGUE ','ALLERGY ', 'WHEEZING', 'ALCOHOL CONSUMING','COUGHING', 'SHORTNESS OF BREATH','SWALLOWING DIFFICULTY', 'CHEST PAIN']
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

genre = st.number_input("Enter your Age (Integer) : ", min_value=1, max_value=105)
try:
    X_inner.append(int(genre))
except:
    X_inner.append(50)
genre = st.radio(
    "Do you Smoke?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
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
    "Are your smoking/drinkings habits influenced by peer pressure (select No, if this does not apply to you)?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you experiencing any Chronic Diseases?",
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
    "Do you have any Allergies?",
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
    "Do you consume Alcohol?",
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
    "Do you suffer from any Shortness of Breath?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Do you suffer from any Swallowing Difficulty?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)
genre = st.radio(
    "Are you suffering from Chest Pain?",
    ('Yes', 'No'))
if genre == "Yes":
    X_inner.append(2)
else:
    X_inner.append(1)

def getDiagnosis():
    X_test.append(X_inner)
    y_pred = model.predict(X_test)
    if y_pred == 0:
        diagnosis = "No Lung Cancer Predicted (Based on given symptoms)"
        st.subheader(f"{diagnosis}")
        st.success('Prediction Released! ✅ - Your symptoms suggest you are not suffering from Lung Cancer.')
    else:
        diagnosis = "Lung Cancer Predicted (Based on given symptoms)"
        st.subheader(f"{diagnosis}")
        st.success('Prediction Released! ✅ - Your symptoms align with common symptoms of Lung Cancer. We suggest you seek medical attention and get a proper diagnosis as a precaution for any health issues.')


submitBtn = st.button("Get Diagnosis", on_click=getDiagnosis,disabled=False)






# if genre == 'Yes':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn't select comedy.")
