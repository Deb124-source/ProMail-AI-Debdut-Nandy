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
    page_title="Grammar Checker",
    page_icon="",
    layout="wide"
)

st.title("AI Grammar Checker")

st.write(
    "Correct grammar, punctuation and improve writing quality."
)

st.divider()

email = st.text_area(
    "Paste your email",
    height=300,
    placeholder="Paste your email here..."
)

generate = st.button(
    "Check Grammar",
    use_container_width=True
)

if generate:

    if email.strip() == "":

        error_message("Please paste an email.")

    else:

        prompt = f"""
You are an expert English editor.

Analyze the email below.

Return your response in the following format.

Grammar Score:
<number>/100

Clarity Score:
<number>/100

Professionalism Score:
<number>/100

Mistakes Found:
- bullet list

Suggestions:
- bullet list

Corrected Email:

<corrected email>

Email:

{email}
"""

        with loading():

            response = ask_gemini(prompt)

        success_message()

        st.subheader("Grammar Report")

        st.markdown(response)

        st.divider()

        prompt2 = f"""
Correct only the grammar and punctuation.

Do not change the meaning.

Return ONLY the corrected email.

Email:

{email}
"""

        corrected = ask_gemini(prompt2)

        left, right = st.columns(2)

        with left:

            st.subheader("Original Email")

            st.text_area(
                "",
                value=email,
                height=320,
                disabled=True
            )

            display_text_statistics(email)

        with right:

            st.subheader("Corrected Email")

            st.text_area(
                "",
                value=corrected,
                height=320
            )

            display_text_statistics(corrected)

        compare_statistics(
            email,
            corrected
        )

        download_txt(
            corrected,
            "corrected_email.txt"
        )

        save_history(
            "Grammar Checker",
            "Grammar",
            "Corrected",
            corrected
        )
