import streamlit as st 
import pandas as pd
from PyPDF2 import PdfReader

st.title("Streamlit Text input")
name = st.text_input("Enter your name:")

if name:                #if a name is input then only this is executed
    st.write(f"Hello, {name}")
    
#Create slider
age = st.slider("Select your age:",0,100,15)
st.write(f"Your age is {age}")

#Dropdown 
options = ["", "C", "R", "Python", "Java", "Ruby"]
choice = st.selectbox("Choose your favourite language:", options)

if choice:  # Check if a valid option is selected
    st.write(f"You selected {choice}")
    
# uploading pdf file

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    st.text_area("Extracted Text", pdf_text, height=300)

#upload csv file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)