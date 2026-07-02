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
    page_title="Generate Email",
    page_icon="",
    layout="wide"
)

st.title("Generate Professional Email")

st.write(
    "Generate professional emails using AI."
)

st.divider()

left, right = st.columns(2)

with left:

    email_type = st.selectbox(
        "Email Type",
        [
            "Formal",
            "Informal",
            "Leave Request",
            "Complaint",
            "Apology",
            "Invitation",
            "Job Application",
            "Internship Application",
            "Meeting Request",
            "Thank You",
            "Follow-up"
        ]
    )

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Friendly",
            "Polite",
            "Confident",
            "Persuasive",
            "Empathetic"
        ]
    )

    length = st.selectbox(
        "Length",
        [
            "Short",
            "Medium",
            "Long"
        ]
    )

with right:

    recipient = st.text_input(
        "Recipient Name"
    )

    sender = st.text_input(
        "Your Name"
    )

    subject = st.text_input(
        "Subject"
    )

purpose = st.text_area(
    "Purpose of Email",
    height=220,
    placeholder="Describe what you want this email to achieve..."
)

st.divider()

generate = st.button(
    "Generate Email",
    use_container_width=True
)

if generate:

    if purpose.strip() == "":

        error_message("Please enter the purpose of the email.")

    else:

        prompt = f"""
You are an expert email writer.

Write a professional email.

Email Type:
{email_type}

Tone:
{tone}

Recipient:
{recipient}

Sender:
{sender}

Subject:
{subject}

Purpose:
{purpose}

Length:
{length}

Requirements:

Use proper greeting.

Use professional formatting.

Use paragraphs.

End with an appropriate closing.

Return ONLY the email.
"""

        with loading():

            email = ask_gemini(prompt)

        success_message()

        st.subheader("Generated Email")

        st.text_area(
            "",
            value=email,
            height=350
        )

        display_text_statistics(email)

        download_txt(
            email,
            "generated_email.txt"
        )

        save_history(
            subject,
            email_type,
            tone
        )
