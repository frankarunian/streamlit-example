import streamlit as st
from transformers import pipeline

# Title of the web application
st.title('SumText: Simple Text Summarization App')

# Subheader or instructions
st.subheader('Enter the text you would like to summarize below:')

# Text area for user input
user_input = st.text_area("Text Input", "Type Here or Paste the text you want to summarize...", height=250)

# Initialize the Hugging Face summarization pipeline
summarizer = pipeline("summarization")

# Button to trigger summarization
if st.button('Summarize'):
    if user_input:
        # Perform summarization
        summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
        # Display the results
        st.subheader('Summary')
        st.write(summary[0]['summary_text'])
    else:
        # Error message for no input
        st.error("Please input some text to summarize.")

# Optional: About section at the end
st.sidebar.header('About SumText')
st.sidebar.info('This application is powered by Streamlit and Hugging Face’s transformers library for easy and quick text summarization.')
