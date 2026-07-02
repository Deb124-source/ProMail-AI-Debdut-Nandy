import streamlit as st

from utils.gemini import ask_gemini
from utils.helper import (
    loading,
    success_message,
    error_message
)

st.set_page_config(
    page_title="Email Quality Scorer",
    page_icon="",
    layout="wide"
)

st.title(" AI Email Quality Scorer")

email = st.text_area(
    "Paste your email",
    height=300
)

analyze = st.button(
    "Analyze",
    use_container_width=True
)

if analyze:

    if email.strip() == "":
        error_message("Please paste an email.")

    else:

        prompt = f"""
Evaluate this email.

Provide:

Overall Score

Strengths

Weaknesses

Professionalism

Grammar

Clarity

Suggestions

Email:

{email}
"""

        with loading():
            report = ask_gemini(prompt)

        success_message()

        st.markdown(report)
