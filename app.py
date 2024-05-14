import pickle

import streamlit as st 


diabetes_model = pickle.load(open('Models/Diabetes.sav' , 'rb'))
heart_disease_model = pickle.load(open('Models/Heart.sav' , 'rb'))
parkinsons_model = pickle.load(open('Models/Parkinsons.sav' , 'rb'))

options = st.sidebar.selectbox(
    'Multiple Disease Prediction System' , 
    options = [ 
        'Diabetes Prediction' , 
        'Heart Disease Prediction' , 
        'Parkinsons Prediction'
    ]
)

tab_1 , tab_2 , tab_3 = st.tabs([
    'Diabetes Prediction' , 
    'Heart Disease Prediction' , 
    'Parkinsons Prediction'
])

with tab_1 : 

    st.title('Diabetes Prediction')

    col_1 , col_2 , col_3 = st.columns(3)
    
    Pregnancies = col_1.text_input('Number of Pregnancies')
    SkinThickness = col_1.text_input('Skin Thickness value')
    DiabetesPedigreeFunction = col_1.text_input('Diabetes Pedigree Function value')
        
    Glucose = col_2.text_input('Glucose Level')
    Insulin = col_2.text_input('Insulin Level')
    Age = col_3.text_input('Age of the Person')

    BloodPressure = col_3.text_input('Blood Pressure value')
    BMI = col_3.text_input('BMI value')
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result') : 
        
        diab_prediction = diabetes_model.predict([[
            float(Pregnancies), float(Glucose), 
            float(BloodPressure), float(SkinThickness), 
            float(Insulin), float(BMI), 
            float(DiabetesPedigreeFunction), float(Age)
        ]])

        if (diab_prediction[0] == 1) : diab_diagnosis = 'The person is diabetic'
        else : diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

with tab_2 : 

    st.title('Heart Disease Prediction using ML')
    
    col_1 , col_2 , col_3 = st.columns(3)
    

    age = col_1.text_input('Age')
    trestbps = col_1.text_input('Resting Blood Pressure')
    restecg = col_1.text_input('Resting Electrocardiographic results')
    oldpeak = col_1.text_input('ST depression induced by exercise')
    thal = col_1.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    sex = col_2.text_input('Sex')
    chol = col_2.text_input('Serum Cholestoral in mg/dl')
    thalach = col_2.text_input('Maximum Heart Rate achieved')
    slope = col_2.text_input('Slope of the peak exercise ST segment')

    cp = col_3.text_input('Chest Pain types')
    fbs = col_3.text_input('Fasting Blood Sugar > 120 mg/dl')
    exang = col_3.text_input('Exercise Induced Angina')
    ca = col_3.text_input('Major vessels colored by flourosopy')

    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):


        heart_prediction = heart_disease_model.predict([[
            float(age), float(sex),
            float(cp), float(trestbps),
            float(chol), float(fbs),
            float(restecg), float(thalach),
            float(exang), float(oldpeak),
            float(slope), float(ca),
            float(thal)
        ]])

        if (heart_prediction[0] == 1) : heart_diagnosis = 'The person is having heart disease'
        else : heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

with tab_3 : 

    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5) 

    fo = col1.text_input('MDVP:Fo(Hz)')
    RAP = col1.text_input('MDVP:RAP')
    APQ3 = col1.text_input('Shimmer:APQ3')
    HNR = col1.text_input('HNR')
    D2 = col1.text_input('D2')

    fhi = col2.text_input('MDVP:Fhi(Hz)')
    PPQ = col2.text_input('MDVP:PPQ')
    APQ5 = col2.text_input('Shimmer:APQ5')
    RPDE = col2.text_input('RPDE')

    flo = col3.text_input('MDVP:Flo(Hz)')
    DDP = col3.text_input('Jitter:DDP')
    APQ = col3.text_input('MDVP:APQ')
    DFA = col3.text_input('DFA')
    spread1 = col3.text_input('spread1')

    Jitter_percent = col4.text_input('MDVP:Jitter(%)')
    Shimmer = col4.text_input('MDVP:Shimmer')
    DDA = col4.text_input('Shimmer:DDA')
    Jitter_Abs = col5.text_input('MDVP:Jitter(Abs)')
    Shimmer_dB = col5.text_input('MDVP:Shimmer(dB)')
    NHR = col5.text_input('NHR')
    spread2 = col5.text_input('spread2')
    PPE = col5.text_input('PPE')
    

    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result") : 
        
        parkinsons_prediction = parkinsons_model.predict([[
            float(fo), float(fhi), 
            float(flo), float(Jitter_percent), 
            float(Jitter_Abs), float(RAP), 
            float(PPQ), float(DDP), 
            float(Shimmer), float(Shimmer_dB), 
            float(APQ3), float(APQ5), 
            float(APQ), float(DDA), 
            float(NHR), float(HNR), 
            float(RPDE), float(DFA), 
            float(spread1), float(spread2), 
            float(D2), float(PPE)
        ]])

        if (parkinsons_prediction[0] == 1) : parkinsons_diagnosis = "The person has Parkinson's disease"
        else : parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
