import streamlit as st
import generator

# --- Page config ---
st.set_page_config(page_title="Bunseiki", page_icon="📝", layout="centered")

# --- Sidebar ---
st.sidebar.title("About Bunseiki")
st.sidebar.markdown(
    """
    **Bunseiki** is a Japanese sentence generator for language learners. 
    
    - Enter a Japanese word (kanji, kana, or romaji)
    - Get a JLPT N3-level example sentence
    - See the English translation
    
    _Powered by OpenAI GPT-4.1_
    """
)

# --- Main App ---
def main():
    st.title("Bunseiki - Japanese Sentence Generator 📝")
    st.markdown("Enter a Japanese word to get a contextual example sentence.")

    word = st.text_input(
        "Enter your word 👇", 
        placeholder="e.g. 勉強 (study)",
        help="Type a Japanese word (kanji, kana, or romaji)"
    )

    if word:
        with st.spinner("Generating sentence..."):
            try:
                result = generator.generate_sentence(word)
                st.success("Here's your example:")
                st.markdown("**Sentence:**")
                st.code(result.sentence, language="ja")
                st.markdown("**Translation:**")
                st.code(result.translation, language="en")
            except Exception as e:
                st.error(f"❌ Failed to generate sentence: {e}")
                st.info("Try a different word or check your connection.")
        st.divider()

    st.caption("Made with ❤️ by Bunseiki. [Source](https://github.com/jgasteiz/bunseiki)")

if __name__ == "__main__":
    main()
