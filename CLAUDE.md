# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Bunseiki is a Japanese sentence generator Streamlit web application that creates contextual Japanese sentences for language learning. The app uses OpenAI's GPT-4.1 via pydantic-ai to generate JLPT N3-level sentences with English translations, plus browser-based text-to-speech for pronunciation practice.

## Architecture

- **streamlit_app.py**: Main Streamlit application with UI, session state management, and browser-based TTS functionality using Web Speech API
- **generator.py**: Core AI sentence generation using pydantic-ai agent framework with structured dataclass outputs
- **requirements.txt**: Python dependencies (streamlit, pydantic-ai==1.0.3, python-dotenv==1.1.1, watchdog)
- **.streamlit/config.toml**: Streamlit configuration with dark theme settings
- **plans/**: Contains improvement plans for the generator module

The app follows a simple two-layer architecture:
1. Streamlit frontend handles UI, user input, session state, and browser-based TTS with unique button IDs
2. Generator module uses pydantic-ai to create structured AI responses via OpenAI GPT-4.1 API

## Development Commands

### Setup and Running
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py

# Run with environment variable (if not using .env file)
OPENAI_API_KEY="your_key" streamlit run streamlit_app.py
```

### Environment Setup
- Copy `.env.example` to `.env` and add your OpenAI API key
- Requires OpenAI API access for GPT-4.1
- The app uses `python-dotenv` to automatically load environment variables

## Key Technical Details

### AI Generation
- Uses pydantic-ai 1.0.3 for structured AI outputs with dataclass-based response types (`OutputType`)
- Agent configured with specific instructions for JLPT N3-level Japanese sentence generation
- Structured output ensures consistent format: `sentence` (Japanese) and `translation` (English)

### TTS Implementation
- Browser-based text-to-speech using Web Speech API
- Generates unique button IDs using hash of text content: `tts_{abs(hash(text)) % 10000}`
- Japanese language settings: `lang='ja-JP'`, `rate=0.9`, `pitch=1.0` for optimal pronunciation
- Attempts to find and use Japanese-specific voices when available
- Visual feedback with button state changes (Play → Playing... → Play)

### UI/UX Features
- Session state management for text input clearing after successful generation
- Streamlit sidebar with app information and instructions
- Dark theme configuration via `.streamlit/config.toml`
- Error handling with user-friendly messages
- Loading spinner during sentence generation

### Code Structure
- `create_japanese_tts_display()`: Generates HTML/JavaScript for TTS buttons in streamlit_app.py:27
- `generate_sentence()`: Main AI generation function in generator.py:26
- `OutputType`: Dataclass defining structured output format in generator.py:6

## Known Improvement Areas

Based on `plans/generator-improvements.md`:
- Docstring accuracy in generator.py (currently says "drills" instead of "sentences")
- Input validation for empty/whitespace input
- Better error handling for API failures
- More explicit AI instructions for Japanese language requirements
- Optional: configurable model selection and logging