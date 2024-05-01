import streamlit as st
from transformers import pipeline

st.title('SumText: Text Summarization App')

user_input = st.text_area("Text Input", "Type here or paste the text you want to summarize...", height=300)
summarizer = pipeline("summarization")

if st.button('Summarize'):
    if user_input:
        summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
        st.write(summary[0]['summary_text'])
    else:
        st.error("Please enter some text to summarize.")
