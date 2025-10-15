import dotenv

dotenv.load_dotenv()

import streamlit as st
from streamlit.components import v1 as v1_components


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
    - 🔊 **NEW**: Click play buttons to hear Japanese pronunciation
    
    _Powered by OpenAI GPT-4.1_
    """
)

def create_copy_button(text, label="Copy"):
    """
    Create a copy button that copies text to clipboard on click
    """
    button_id = f"copy_{abs(hash(text)) % 10000}"

    html_code = f"""
    <html>
        <body style="margin: 0;">
            <button id="btn_{button_id}" onclick="copyText_{button_id}()"
                    style="background: linear-gradient(45deg, #4CAF50, #45a049);
                           color: white;
                           border: none;
                           padding: 6px 12px;
                           border-radius: 4px;
                           cursor: pointer;
                           font-size: 12px;
                           transition: all 0.2s ease;
                           margin: 4px 0;">
                📋 {label}
            </button>
        </body>
    </html>

    <script>
    function copyText_{button_id}() {{
        const text = `{text}`;
        const button = document.getElementById('btn_{button_id}');

        if (navigator.clipboard && navigator.clipboard.writeText) {{
            navigator.clipboard.writeText(text)
                .then(() => {{
                    console.log('Copied to clipboard');
                    button.style.background = 'linear-gradient(45deg, #2196F3, #1976D2)';
                    button.innerHTML = '✓ Copied!';
                    setTimeout(() => {{
                        button.style.background = 'linear-gradient(45deg, #4CAF50, #45a049)';
                        button.innerHTML = '📋 {label}';
                    }}, 2000);
                }})
                .catch(err => {{
                    console.error('Failed to copy:', err);
                    button.style.background = 'linear-gradient(45deg, #f44336, #d32f2f)';
                    button.innerHTML = '❌ Failed';
                    setTimeout(() => {{
                        button.style.background = 'linear-gradient(45deg, #4CAF50, #45a049)';
                        button.innerHTML = '📋 {label}';
                    }}, 2000);
                }});
        }} else {{
            alert('Clipboard access not supported in this browser');
        }}
    }}
    </script>
    """

    v1_components.html(html_code, height=35)

def create_japanese_tts_display(text):
    """
    Create a display component for Japanese text with TTS play button
    """
    # Generate a unique ID for this instance
    button_id = f"tts_{abs(hash(text)) % 10000}"
    
    html_code = f"""
    <html>
        <body style="margin: 0;">
            <button onclick="speakJapanese_{button_id}()" 
                    style="background: linear-gradient(45deg, #ff4b4b, #ff6b6b); 
                           color: white;
                           border: none;
                           padding: 8px 12px; 
                           border-radius: 4px;
                           cursor: pointer;
                           font-size: 12px; display: flex; align-items: center;
                           transition: all 0.2s ease;">
                🔊 Play
            </button>
        </body>
    
    </html>
    
    <script>
    function speakJapanese_{button_id}() {{
        const text = `{text}`;
        
        if ('speechSynthesis' in window) {{
            // Cancel any ongoing speech
            window.speechSynthesis.cancel();
            
            // Create utterance with Japanese-optimized settings
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'ja-JP';
            utterance.rate = 0.9;  // Slightly slower for clarity
            utterance.pitch = 1.0;
            utterance.volume = 1.0;
            
            // Try to find and use a Japanese voice
            const voices = window.speechSynthesis.getVoices();
            const japaneseVoice = voices.find(voice => 
                voice.lang.includes('ja') || 
                voice.lang.includes('JP') ||
                voice.name.toLowerCase().includes('japanese')
            );
            
            if (japaneseVoice) {{
                utterance.voice = japaneseVoice;
                console.log('Using Japanese voice:', japaneseVoice.name);
            }} else {{
                console.log('No Japanese voice found, using default');
            }}
            
            // Add event listeners for feedback
            utterance.onstart = function() {{
                console.log('Speech started');
                const button = document.querySelector('button[onclick="speakJapanese_{button_id}()"]');
                if (button) {{
                    button.style.background = 'linear-gradient(45deg, #28a745, #20c997)';
                    button.innerHTML = '🔊 Playing...';
                }}
            }};
            
            utterance.onend = function() {{
                console.log('Speech ended');
                const button = document.querySelector('button[onclick="speakJapanese_{button_id}()"]');
                if (button) {{
                    button.style.background = 'linear-gradient(45deg, #ff4b4b, #ff6b6b)';
                    button.innerHTML = '🔊 Play';
                }}
            }};
            
            utterance.onerror = function(event) {{
                console.error('Speech error:', event.error);
                const button = document.querySelector('button[onclick="speakJapanese_{button_id}()"]');
                if (button) {{
                    button.style.background = 'linear-gradient(45deg, #dc3545, #e74c3c)';
                    button.innerHTML = '❌ Error';
                    setTimeout(() => {{
                        button.style.background = 'linear-gradient(45deg, #ff4b4b, #ff6b6b)';
                        button.innerHTML = '🔊 Play';
                    }}, 2000);
                }}
            }};
            
            // Speak the text
            window.speechSynthesis.speak(utterance);
        }} else {{
            alert('Text-to-speech is not supported in this browser. Please use Chrome, Firefox, Safari, or Edge.');
        }}
    }}
    
    // Load voices when available (some browsers need this)
    if (window.speechSynthesis.onvoiceschanged !== undefined) {{
        window.speechSynthesis.onvoiceschanged = function() {{
            console.log('Voices loaded:', window.speechSynthesis.getVoices().length);
        }};
    }}
    </script>
    """
    
    v1_components.html(html_code, height=40)

# --- Main App ---
def main():
    import generator

    st.title("Bunseiki - Japanese Sentence Generator 📝")
    st.markdown("Enter a Japanese word to get a contextual example sentence.")

    # Initialize session state for text input
    if "text_input" not in st.session_state:
        st.session_state.text_input = ""

    word = st.text_input(
        "Enter your word 👇",
        value=st.session_state.text_input,
        placeholder="e.g. 勉強 (study)",
        help="Type a Japanese word (kanji, kana, or romaji)",
        key="word_input"
    )

    if word:
        with st.spinner("Generating sentence..."):
            try:
                result = generator.generate_sentence(word)
                st.success("Here's your example:")
                st.markdown("**Sentence:**")
                st.code(result.sentence, language="ja")
                # Add TTS and copy button side by side
                col1, col2 = st.columns([1, 4])
                with col1:
                    create_japanese_tts_display(result.sentence)
                with col2:
                    create_copy_button(result.sentence, "Copy Sentence")

                st.markdown("**Translation:**")
                st.code(result.translation, language="en")
                create_copy_button(result.translation, "Copy Translation")

                # Clear the text input after successful generation
                st.session_state.text_input = ""
            except Exception as e:
                st.error(f"❌ Failed to generate sentence: {e}")
                st.info("Try a different word or check your connection.")
        st.divider()

    st.caption("Made with ❤️ by Bunseiki. [Source](https://github.com/jgasteiz/bunseiki)")

if __name__ == "__main__":
    main()
