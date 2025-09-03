# Bunseiki - Japanese Sentence Generator 📝

A Streamlit web application that generates contextual Japanese sentences for language learning practice. Enter a Japanese word and get a sentence at JLPT N3 level along with an English translation.

## Features

- **Smart Sentence Generation**: Uses OpenAI's GPT-4.1 to create contextually appropriate sentences
- **JLPT N3 Level**: Generates sentences at intermediate difficulty level
- **Bilingual Output**: Provides both Japanese sentence and English translation
- **Simple Interface**: Clean Streamlit web interface for easy use

## How it Works

1. Enter a Japanese word in the text input field
2. The application uses AI to generate a sentence incorporating that word
3. Receive both the Japanese sentence and English translation for context

## Installation & Usage

### Prerequisites

- Python 3.7+
- OpenAI API access (for GPT-4.1)

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bunseiki
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable

4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```
   Or run it passing the env variable directly:
   ```bash
   OPENAI_API_KEY="your_openai_api_key" streamlit run streamlit_app.py
   ```

## Dependencies

- `streamlit` - Web application framework
- `pydantic-ai` - AI agent framework with structured outputs

## Use Cases

- Japanese language learners wanting to see words in context
- Practice reading comprehension with varied sentence structures
- Building vocabulary through contextual examples
- JLPT N3 level preparation

---

*Bunseiki (文析) - Helping you understand Japanese sentences in context*
