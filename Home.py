import streamlit as st
import os

#Title of the home page
st.header(":blue[Flipkart Laptop Price Prediction Data App :desktop_computer]")
#Using subheader
st.write('By: :red[Ruthvik Bathala]')

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resourses")



