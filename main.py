import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

def stroke_prediction(input_data):
   
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict_proba(input_data_reshaped)[:, 1][0]
    # print(prediction*100)
    return f'You have {prediction*100}% chance of having a stroke.'
    # if (prediction[0] == 0):
    #     return 'The person does not have a stroke'
    # else:
    #     return 'The person have a stroke'

def main():
    st.title('Heart Stroke Prediction')

    gender = st.radio("Gender",('Male', 'Female', 'Other'))
    if(gender == 'Male'):
        gender = 1
    elif(gender == 'Female'):
        gender = 0
    else:
        gender = 2

    age = st.slider('Age', 1, 120)
    age = (age-43.22661448140902)/(22.61043402711303)

    hypertension = st.radio("Hypertension",('Yes', 'No'))
    if(hypertension == 'Yes'):
        hypertension = 1
    else:
        hypertension = 0

    heart_disease = st.radio("Heart Disease",('Yes', 'No'))
    if(heart_disease == 'Yes'):
        heart_disease = 1
    else:
        heart_disease = 0

    ever_married = st.radio("Ever Married",('Yes', 'No'))
    if(ever_married == 'Yes'):
        ever_married = 1
    else:
        ever_married = 0

    work_type = st.radio("Work Type",('Government Job', 'Never Worked', 'Private', 'Self-employed', 'Children'))
    if(work_type == 'Government Job'):
        work_type = 0
    elif(work_type == 'Never Worked'):
        work_type = 1
    elif(work_type == 'Private'):
        work_type = 2
    elif(work_type == 'Self-employed'):
        work_type = 3
    else:
        work_type = 4
    
    Residence_type = st.radio("Residence Type",('Rural', 'Urban'))
    if(Residence_type == "Rural"):
        Residence_type = 0
    else:
        Residence_type = 1

    avg_glucose_level = st.number_input('Average Glucose Level')
    avg_glucose_level = (avg_glucose_level-106.14767710371795)/(45.27912905705893)

    bmi = st.number_input('BMI')
    bmi = (bmi-28.90337865973328)/(7.698534094073452)

    smoking_status = st.radio("Smoking Status",('Formerly Smoked', 'Never Smoked', 'Smokes', 'Unknown'))
    if(smoking_status == "Formerly Smoked"):
        smoking_status = 1
    elif(smoking_status == "Never Smoked"):
        smoking_status = 2
    elif(smoking_status == "Smokes"):
        smoking_status = 3
    else:
        smoking_status = 0

    diagnosis = ''

    if st.button('Stroke Test Result'):
        diagnosis = stroke_prediction([gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status])

    st.success(diagnosis)

if __name__ == '__main__':
    main()

