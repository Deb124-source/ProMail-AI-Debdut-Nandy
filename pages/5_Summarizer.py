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
    page_title="Email Summarizer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Email Summarizer")

st.write(
    "Summarize long emails into easy-to-read insights."
)

st.divider()

email = st.text_area(
    "Paste Long Email",
    height=320,
    placeholder="Paste the email you want to summarize..."
)

summary_style = st.selectbox(
    "Summary Style",
    [
        "Executive Summary",
        "Bullet Points",
        "Detailed Summary",
        "Action Items Only",
        "Meeting Notes"
    ]
)

generate = st.button(
    "📄 Generate Summary",
    use_container_width=True
)

if generate:

    if email.strip() == "":

        error_message(
            "Please paste an email."
        )

    else:

        prompt = f"""
You are an AI Email Assistant.

Summarize the following email.

Summary Style:
{summary_style}

Return:

## Executive Summary

## Key Points

## Action Items

## Important Dates

## People Mentioned

Email:

{email}
"""

        with loading():

            summary = ask_gemini(prompt)

        success_message()

        st.subheader("Summary")

        st.markdown(summary)

        st.divider()

        st.subheader("Original Email Statistics")

        display_text_statistics(email)

        st.subheader("Summary Statistics")

        display_text_statistics(summary)

        st.divider()

        download_txt(
            summary,
            "email_summary.txt"
        )

        save_history(
            "Email Summary",
            "Summary",
            summary_style,
            summary
        )
