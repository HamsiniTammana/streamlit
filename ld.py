import streamlit as st
import joblib
st.title('Loan Approval Process Automation')
model=joblib.load('C:/Users/Admin/Downloads/loan_data1.csv')
gender=st.number_input("enter gender Male:0 Female:1")
married=st.number_input("enter Martial status Married:1 UnMarried:0")
income=st.number_input("enter applicant income in thousands")
la=st.number_input("enter loan amount in thousands")
if st.button('predict Approval'):
    prediction=model.predict([[gender,married,income,la]])
    if predictions=='y':
        st.text('Loan Approval')
    else:
        st.text('Loan Rejected')
