import streamlit as st

from utils.gemini import ask_gemini
from utils.helper import (
    loading,
    success_message,
    error_message
)

st.set_page_config(
    page_title="Subject Generator",
    page_icon="",
    layout="wide"
)

st.title("AI Subject Line Generator")

purpose = st.text_area(
    "Describe your email",
    height=200
)

generate = st.button(
    "Generate Subject Lines",
    use_container_width=True
)

if generate:

    if purpose.strip() == "":
        error_message("Please describe your email.")

    else:

        prompt = f"""
Generate 10 professional subject lines.

Purpose:

{purpose}

Return ONLY a numbered list.
"""

        with loading():
            subjects = ask_gemini(prompt)

        success_message()

        st.markdown(subjects)
