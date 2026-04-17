import streamlit as st
from core.similarity import compute_similarity

st.set_page_config(page_title="Code Similarity Detector", layout="wide")

st.title("🧠 Code Similarity Detector")

col1, col2 = st.columns(2)

with col1:
    code1 = st.text_area("Enter Code 1", height=300)

with col2:
    code2 = st.text_area("Enter Code 2", height=300)

if st.button("Compare"):
    if code1 and code2:
        score = compute_similarity(code1, code2)
        st.success(f"Similarity Score: {score}%")
    else:
        st.warning("Please enter both code snippets")