import streamlit as st
import joblib

model = joblib.load("lr_model")
st.title("Salary Prediction App")
st.header("This is done using Streamlit")
st.subheader("The algorithm used is Linear Regression")
st.text("Please enter the years of experience and click on PREDICT button")

years = st.number_input('Enter the years of Experience', min_value = 0.0, max_value = 15.0, value = 5.5, step = 0.5)

if st.button('PREDICT'):
  sal = model.predict([[years]])
  st.subheader("The expected salary is" + str(sal))
