import streamlit as st

st.set_page_config(
    page_title="ProMailAI",
    page_icon="",
    layout="wide"
)

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("ProMail AI")

st.write(
    """
Generate professional emails, improve writing,
reply intelligently, summarize emails,
translate content and much more.
"""
)

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.info("Generate Emails")

with c2:
    st.success("Grammar Checker")

with c3:
    st.warning("Translator")

c4, c5, c6 = st.columns(3)

with c4:
    st.info("Summarizer")

with c5:
    st.success("Email Analyzer")

with c6:
    st.warning("Signature Generator")

st.divider()

st.header("Features")

features = [
    "Generate Professional Emails",
    "Reply to Emails",
    "Improve Existing Emails",
    "Grammar Checker",
    "Email Summarizer",
    "Translator",
    "Tone Changer",
    "Email Analyzer",
    "Signature Generator",
]

for feature in features:
    st.markdown(f"{feature}")

st.success("Use the sidebar to access all tools.")

st.divider()

st.info("Use the **left sidebar** to navigate between all the Email Suite tools.")
