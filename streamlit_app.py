import streamlit as st

import generator

st.title("🎈 Japanese sentence generator")
word = st.text_input(
    "Enter your word 👇",
)

if word:
    st.write(f"You entered: {word}. Generating sentence...")
    sentence = generator.generate_sentence(word)
    st.write(sentence)
