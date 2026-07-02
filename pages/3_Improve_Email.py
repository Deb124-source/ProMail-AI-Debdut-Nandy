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
    page_title="Improve Email",
    page_icon="",
    layout="wide"
)

st.title("Improve Existing Email")

st.write(
    "Rewrite your email with AI while keeping the original meaning."
)

st.divider()

left, right = st.columns(2)

with left:

    style = st.selectbox(
        "Improvement Style",
        [
            "More Professional",
            "More Friendly",
            "More Formal",
            "More Concise",
            "More Persuasive",
            "More Empathetic",
            "More Confident",
            "More Conversational"
        ]
    )

with right:

    keep_length = st.selectbox(
        "Length",
        [
            "Keep Original",
            "Shorter",
            "Longer"
        ]
    )

extra = st.text_input(
    "Additional Instructions (Optional)"
)

email = st.text_area(
    "Paste Your Email",
    height=320,
    placeholder="Paste your email here..."
)

generate = st.button(
    "Improve Email",
    use_container_width=True
)

if generate:

    if email.strip() == "":

        error_message(
            "Please paste an email first."
        )

    else:

        prompt = f"""
You are a professional email editor.

Rewrite the following email.

Improvement Style:
{style}

Length:
{keep_length}

Additional Instructions:
{extra}

Requirements:

Improve readability.

Improve grammar.

Improve sentence structure.

Keep the original meaning.

Return ONLY the improved email.

Email:

{email}
"""

        with loading():

            improved_email = ask_gemini(prompt)

        success_message()

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.subheader("Original Email")

            st.text_area(
                "",
                value=email,
                height=350,
                disabled=True
            )

            display_text_statistics(email)

        with c2:

            st.subheader("Improved Email")

            st.text_area(
                "",
                value=improved_email,
                height=350
            )

            display_text_statistics(improved_email)

        st.divider()

        download_txt(
            improved_email,
            "improved_email.txt"
        )

        save_history(
            "Improve Email",
            "Improved",
            style,
            improved_email
        )
