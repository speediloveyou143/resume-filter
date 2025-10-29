import streamlit as st
import requests as req
from PyPDF2 import PdfReader

st.title("upload your resumes here")
try:
    uploaded_resume=st.file_uploader("upload your pdf")
    if uploaded_resume:
        pdf=PdfReader(uploaded_resume)
        text=""
        for page in pdf.pages:
            text=text+page.extract_text()
        
        result=req.post("url",json={"resume_text":text})
        if result:
            st.success("file uploaded")
        else:
            st.warning("file uploading failed")
except:
    st.warning("file upload filed")