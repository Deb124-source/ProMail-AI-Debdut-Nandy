import streamlit as st

from utils.gemini import ask_gemini

from utils.helper import (
    display_text_statistics,
    compare_statistics,
    download_txt,
    loading,
    success_message,
    error_message,
    save_history
)

st.set_page_config(
    page_title="Tone Changer",
    page_icon="",
    layout="wide"
)

st.title("AI Email Tone Changer")

st.write(
    "Rewrite your email in different tones while preserving the original meaning."
)

st.divider()

left, right = st.columns(2)

with left:

    tone = st.selectbox(
        "Choose New Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Casual",
            "Persuasive",
            "Empathetic",
            "Confident",
            "Assertive",
            "Diplomatic",
            "Apologetic",
            "Customer Support",
            "Sales Pitch",
            "Executive",
            "Academic"
        ]
    )

with right:

    length = st.selectbox(
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
    "Paste Email",
    height=320,
    placeholder="Paste your email here..."
)

generate = st.button(
    "Change Tone",
    use_container_width=True
)

if generate:

    if email.strip() == "":

        error_message("Please paste an email.")

    else:

        prompt = f"""
You are a professional communication expert.

Rewrite the following email.

Desired Tone:
{tone}

Length:
{length}

Additional Instructions:
{extra}

Requirements:

Maintain the original meaning.

Improve readability.

Use proper grammar.

Return ONLY the rewritten email.

Email:

{email}
"""

        with loading():

            rewritten = ask_gemini(prompt)

        success_message()

        st.divider()

        left, right = st.columns(2)

        with left:

            st.subheader("Original Email")

            st.text_area(
                "",
                value=email,
                height=350,
                disabled=True
            )

            display_text_statistics(email)

        with right:

            st.subheader("Rewritten Email")

            st.text_area(
                "",
                value=rewritten,
                height=350
            )

            display_text_statistics(rewritten)

        compare_statistics(
            email,
            rewritten
        )

        st.divider()

        explanation_prompt = f"""
Explain in 3-5 bullet points what changed when rewriting this email into a {tone} tone.

Original Email:
{email}

Rewritten Email:
{rewritten}
"""

        explanation = ask_gemini(explanation_prompt)

        st.subheader("Tone Change Summary")

        st.markdown(explanation)

        download_txt(
            rewritten,
            "tone_changed_email.txt"
        )

        save_history(
            "Tone Changer",
            "Tone Change",
            tone,
            rewritten
        )
