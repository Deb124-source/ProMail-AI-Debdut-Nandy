import streamlit as st

from utils.gemini import ask_gemini

from utils.helper import (
    display_text_statistics,
    download_txt,
    loading,
    success_message,
    error_message,
    save_history
)

st.set_page_config(
    page_title="Email Translator",
    page_icon="",
    layout="wide"
)

st.title("AI Email Translator")

st.write(
    "Translate emails while preserving formatting, tone, and meaning."
)

st.divider()

left, right = st.columns(2)

with left:

    source_language = st.selectbox(
        "Source Language",
        [
            "Auto Detect",
            "English",
            "Hindi",
            "Bengali",
            "Spanish",
            "French",
            "German",
            "Japanese",
            "Chinese",
            "Arabic"
        ]
    )

with right:

    target_language = st.selectbox(
        "Target Language",
        [
            "English",
            "Hindi",
            "Bengali",
            "Spanish",
            "French",
            "German",
            "Japanese",
            "Chinese",
            "Arabic"
        ]
    )

translation_style = st.selectbox(
    "Translation Style",
    [
        "Professional",
        "Formal",
        "Business",
        "Simple",
        "Natural"
    ]
)

email = st.text_area(
    "Paste Email",
    height=320,
    placeholder="Paste the email to translate..."
)

translate = st.button(
    "Translate Email",
    use_container_width=True
)

if translate:

    if email.strip() == "":

        error_message("Please paste an email.")

    else:

        prompt = f"""
You are an expert multilingual translator.

Translate the following email.

Source Language:
{source_language}

Target Language:
{target_language}

Style:
{translation_style}

Requirements:

- Preserve formatting
- Preserve paragraph spacing
- Preserve professional tone
- Translate accurately
- Return ONLY the translated email

Email:

{email}
"""

        with loading():

            translated = ask_gemini(prompt)

        success_message()

        st.subheader("Translated Email")

        st.text_area(
            "",
            translated,
            height=350
        )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("Original")

            display_text_statistics(email)

        with c2:

            st.subheader("Translated")

            display_text_statistics(translated)

        download_txt(
            translated,
            "translated_email.txt"
        )

        save_history(
            "Translator",
            "Translation",
            target_language,
            translated
        )
