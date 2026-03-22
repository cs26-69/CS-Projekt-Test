import streamlit as st

st.title("Hello World!")

st.title("This document is going to be used for our group project.")

group_grade = st.slider("Input our group grade on a scale from 1 to 6", 1, 6)

if group_grade == 6:
  st.write("Good choice")
