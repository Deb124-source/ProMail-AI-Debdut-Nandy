import streamlit as st
import json

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
    page_title="Email Analyzer",
    page_icon="",
    layout="wide"
)

st.title("AI Email Analyzer")

st.write(
    "Analyze your email and receive an AI-powered quality report."
)

st.divider()

email = st.text_area(
    "Paste Your Email",
    height=320,
    placeholder="Paste your email here..."
)

analyze = st.button(
    " Analyze Email",
    use_container_width=True
)

if analyze:

    if email.strip() == "":

        error_message("Please paste an email.")

    else:

        prompt = f"""
Analyze the email below.

Return ONLY valid JSON.

{{
"overall_score":95,
"grammar":92,
"clarity":94,
"professionalism":97,
"readability":91,
"tone":"Professional",
"purpose":"Request Meeting",
"verdict":"Excellent",
"issues":[
"issue1",
"issue2"
],
"suggestions":[
"suggestion1",
"suggestion2",
"suggestion3"
]
}}

Email:

{email}
"""

        with loading():

            response = ask_gemini(prompt)

        try:

            # Remove markdown code fences if Gemini adds them
            cleaned = response.replace("```json", "").replace("```", "").strip()

            result = json.loads(cleaned)

            success_message()

            st.header("📊 Overall Report")

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Overall",
                f"{result['overall_score']}/100"
            )

            c2.metric(
                "Verdict",
                result["verdict"]
            )

            c3.metric(
                "Detected Tone",
                result["tone"]
            )

            st.divider()

            st.subheader("Scores")

            st.write("Grammar")
            st.progress(result["grammar"]/100)

            st.write("Clarity")
            st.progress(result["clarity"]/100)

            st.write("Professionalism")
            st.progress(result["professionalism"]/100)

            st.write("Readability")
            st.progress(result["readability"]/100)

            st.divider()

            st.subheader("🎯 Purpose")

            st.info(result["purpose"])

            st.subheader("⚠ Issues Found")

            for issue in result["issues"]:

                st.warning(issue)

            st.subheader("Suggestions")

            for suggestion in result["suggestions"]:

                st.success(suggestion)

            st.divider()

            st.subheader("Statistics")

            display_text_statistics(email)

            download_txt(
                json.dumps(result, indent=4),
                "analysis_report.json"
            )

            save_history(
                "Email Analyzer",
                "Analysis",
                result["tone"],
                json.dumps(result)
            )

        except Exception:

            st.error(
                "Gemini returned an unexpected response. Please try again."
            )
