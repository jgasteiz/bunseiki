import streamlit as st

import generator

st.set_page_config(page_title="Bunseiki", page_icon="📝")

st.title("Bunseiki - Japanese Sentence Generator 📝")

word = st.text_input(
    "Enter your word 👇",
)

if word:
    st.write(f"Generating sentence...")
    result = generator.generate_sentence(word)
    st.code("\n".join([result.sentence, result.translation]))
