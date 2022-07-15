import streamlit as st
import joblib
model = joblib.load('Weather Prediction')
st.title('WEATHER PREDICTOR')
ip = st.number_input('Enter a Year',value=0)
op = model.predict([[ip]])
if st.button('Predict'):
  st.title(op[0])
