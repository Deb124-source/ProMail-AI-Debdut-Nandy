import streamlit as st

from utils.gemini import ask_gemini
from utils.helper import (
    download_txt,
    loading,
    success_message,
    error_message,
    save_history
)

st.set_page_config(
    page_title="Email Templates",
    page_icon="",
    layout="wide"
)

st.title("AI Smart Email Templates")

template = st.selectbox(
    "Choose Template",
    [
        "Leave Request",
        "Job Application",
        "Internship Application",
        "Meeting Request",
        "Follow-up",
        "Complaint",
        "Thank You",
        "Resignation",
        "Promotion Request",
        "Salary Negotiation",
        "Business Proposal",
        "Invitation"
    ]
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Formal",
        "Polite"
    ]
)

details = st.text_area(
    "Describe your situation",
    height=250
)

generate = st.button(
    " Generate Template",
    use_container_width=True
)

if generate:

    if details.strip() == "":
        error_message("Please enter some details.")

    else:

        prompt = f"""
Write a professional email.

Template:
{template}

Tone:
{tone}

Details:
{details}

Return ONLY the email.
"""

        with loading():
            email = ask_gemini(prompt)

        success_message()

        st.text_area(
            "Generated Email",
            email,
            height=350
        )

        download_txt(
            email,
            "template_email.txt"
        )

        save_history(
            template,
            "Template",
            tone,
            email
        )
