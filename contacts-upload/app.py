import streamlit as st

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    file_content = uploaded_file.read()
    name_wih_extension = uploaded_file.name
    path = f"/Users/rakshit.bhasin/Desktop/contact_files/{name_wih_extension}"
    with open(path, 'wb') as file:
        file.write(file_content)
