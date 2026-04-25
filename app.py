import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("My streamlit app")

st.write("hello! your streamlit app is running successfully")

st.write("edit app.py to see live changes.")


# Input
banks = st.number_input("Enter number of banks on UPI", min_value=1)

# Predict
if st.button("Predict"):
    prediction = model.predict([[banks]])
    st.success(f"Predicted Volume: {prediction[0]:.2f} Mn")
