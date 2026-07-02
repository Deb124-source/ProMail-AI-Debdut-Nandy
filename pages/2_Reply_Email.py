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
    page_title="Reply to Email",
    page_icon="📨",
    layout="wide"
)

st.title("📨 AI Email Reply")

st.write(
    "Generate professional replies to emails using Gemini AI."
)

st.divider()

left, right = st.columns(2)

with left:

    tone = st.selectbox(
        "Reply Tone",
        [
            "Professional",
            "Friendly",
            "Polite",
            "Confident",
            "Empathetic",
            "Persuasive"
        ]
    )

    reply_type = st.selectbox(
        "Reply Type",
        [
            "Positive",
            "Neutral",
            "Decline",
            "Apology",
            "Follow-up",
            "Acknowledgement"
        ]
    )

with right:

    sender = st.text_input(
        "Your Name"
    )

    extra_instruction = st.text_input(
        "Extra Instruction (Optional)"
    )

original_email = st.text_area(
    "Paste Original Email",
    height=300,
    placeholder="Paste the received email here..."
)

generate = st.button(
    "🚀 Generate Reply",
    use_container_width=True
)

if generate:

    if original_email.strip() == "":

        error_message(
            "Please paste the original email."
        )

    else:

        prompt = f"""
You are a professional email assistant.

Write a reply.

Original Email:

{original_email}

Reply Tone:

{tone}

Reply Type:

{reply_type}

Sender:

{sender}

Additional Instructions:

{extra_instruction}

Requirements:

Reply naturally.

Use proper greeting.

Maintain professionalism.

Use paragraphs.

Sign off using the sender name.

Return ONLY the reply.
"""

        with loading():

            reply = ask_gemini(prompt)

        success_message()

        st.subheader("Generated Reply")

        st.text_area(
            "",
            value=reply,
            height=350
        )

        display_text_statistics(reply)

        download_txt(
            reply,
            "reply_email.txt"
        )

        save_history(
            "Reply Email",
            "Reply",
            tone,
            reply
        )
