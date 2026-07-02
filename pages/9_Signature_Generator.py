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
    page_title="Signature Generator",
    page_icon="",
    layout="wide"
)

st.title(" AI Professional Signature Generator")

st.write(
    "Create beautiful and professional email signatures."
)

st.divider()

left, right = st.columns(2)

with left:

    full_name = st.text_input("Full Name")

    designation = st.text_input("Designation")

    company = st.text_input("Company")

    email = st.text_input("Email Address")

with right:

    phone = st.text_input("Phone Number")

    website = st.text_input("Website")

    linkedin = st.text_input("LinkedIn URL")

    address = st.text_input("Office Address (Optional)")

style = st.selectbox(

    "Signature Style",

    [

        "Minimal",

        "Corporate",

        "Modern",

        "Elegant"

    ]

)

generate = st.button(

    "Generate Signature",

    use_container_width=True

)

if generate:

    if full_name.strip() == "":

        error_message("Please enter your name.")

    else:

        prompt = f"""
Create a professional email signature.

Name:
{full_name}

Designation:
{designation}

Company:
{company}

Email:
{email}

Phone:
{phone}

Website:
{website}

LinkedIn:
{linkedin}

Address:
{address}

Style:
{style}

Requirements:

Return ONLY the signature.

Make it visually clean.

Use icons when appropriate.
"""

        with loading():

            signature = ask_gemini(prompt)

        success_message()

        st.divider()

        st.subheader("Preview")

        st.code(signature)

        st.divider()

        download_txt(

            signature,

            "email_signature.txt"

        )

        save_history(

            "Signature",

            "Signature",

            style,

            signature

        )
