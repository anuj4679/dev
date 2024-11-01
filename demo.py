import streamlit as st

st.title("Demo App")
first_name=st.text_input("Enter your first name")
second_name=st.text_input("enter your second name")

st.write(first_name + second_name)