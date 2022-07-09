import streamlit as st
import joblib
model = joblib.load('Weather Prediction')
st.title('WEATHER PREDICTOR')
ip = st.text_input('Enter a Year')
op = model.predict([[ip]])
if st.button('Predict'):
  st.title(op[0])
