import streamlit as st
import requests
import logging

st.title("Chat Categorizer Bot")

user_input = st.text_input("Enter a customer message :")

if st.button("Categorize"):
    if user_input:
        response = requests.post("http://127.0.0.1:5000/categorize", json={"message": user_input})
        result = response.json()
        logging.info(f"API Response: {result}")
        st.write(f"API Response: {result}")
        st.success(f"**Category**: {result['category']} ")
    else:
        st.warning("Please enter a message.")
        
