import streamlit as st
from datetime import datetime
import pandas as pd



def word_count(text):
    """Return the number of words."""
    return len(text.split())


def character_count(text):
    """Return the number of characters."""
    return len(text)


def line_count(text):
    """Return the number of lines."""
    return len(text.splitlines())



def display_text_statistics(text):

    c1, c2, c3 = st.columns(3)

    c1.metric("Words", word_count(text))
    c2.metric("Characters", character_count(text))
    c3.metric("Lines", line_count(text))



def download_txt(text, filename="generated_email.txt"):

    st.download_button(
        label="⬇️ Download as TXT",
        data=text,
        file_name=filename,
        mime="text/plain",
        use_container_width=True
    )



def copy_message():

    st.info(
        "Select the generated email and press **Ctrl + C** (Windows) or **Cmd + C** (Mac) to copy."
    )



def save_history(subject, email_type, tone):

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(
        {
            "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Subject": subject,
            "Type": email_type,
            "Tone": tone
        }
    )



def show_history():

    if "history" not in st.session_state:

        st.warning("No emails generated yet.")

        return

    df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )



def clear_history():

    if st.button("Clear History"):

        st.session_state.history = []

        st.success("History Cleared!")



def success_message():

    st.success("Email generated successfully!")



def error_message(msg):

    st.error(msg)



def loading():

    return st.spinner("Generating your email...")


def divider():

    st.markdown("---")
