import streamlit as st
import pandas as pd
from datetime import datetime


# ===========================
# TEXT STATISTICS
# ===========================

def word_count(text):
    return len(text.split())


def character_count(text):
    return len(text)


def line_count(text):
    return len(text.splitlines())


# ===========================
# DISPLAY TEXT STATISTICS
# ===========================

def display_text_statistics(text):

    c1, c2, c3 = st.columns(3)

    c1.metric("Words", word_count(text))
    c2.metric("Characters", character_count(text))
    c3.metric("Lines", line_count(text))


# ===========================
# BEFORE VS AFTER
# ===========================

def compare_statistics(original, improved):

    st.subheader("Before vs After")

    left, right = st.columns(2)

    with left:
        st.metric("Original Words", word_count(original))
        st.metric("Original Characters", character_count(original))

    with right:
        st.metric("Improved Words", word_count(improved))
        st.metric("Improved Characters", character_count(improved))


# ===========================
# DOWNLOAD BUTTON
# ===========================

def download_txt(text, filename="generated_email.txt"):

    st.download_button(
        label="⬇ Download as TXT",
        data=text,
        file_name=filename,
        mime="text/plain",
        use_container_width=True
    )


# ===========================
# SUCCESS MESSAGE
# ===========================

def success_message():

    st.success("✅ Task completed successfully!")


# ===========================
# ERROR MESSAGE
# ===========================

def error_message(message):

    st.error(message)


# ===========================
# LOADING SPINNER
# ===========================

def loading():

    return st.spinner("Processing the Request...")


# ===========================
# DIVIDER
# ===========================

def divider():

    st.markdown("---")


# ===========================
# EMAIL HISTORY
# ===========================

def save_history(subject,
                 email_type,
                 tone,
                 content=""):

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({

        "Date": datetime.now().strftime("%d-%m-%Y %H:%M"),

        "Subject": subject,

        "Type": email_type,

        "Tone": tone,

        "Content": content

    })


# ===========================
# SHOW HISTORY
# ===========================

def show_history():

    if "history" not in st.session_state:

        st.info("No history available.")

        return

    df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ===========================
# CLEAR HISTORY
# ===========================

def clear_history():

    if "history" in st.session_state:

        st.session_state.history = []

        st.success("History cleared successfully!")


# ===========================
# EXPORT HISTORY
# ===========================

def download_history():

    if "history" not in st.session_state:

        st.warning("No history available.")

        return

    df = pd.DataFrame(st.session_state.history)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="⬇ Download History",

        data=csv,

        file_name="email_history.csv",

        mime="text/csv",

        use_container_width=True
    )
