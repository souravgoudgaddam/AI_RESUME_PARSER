import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("🧠 AI Resume Parser & Job Matcher")

# Upload Resume
st.header("📄 Upload Resume")
uploaded_file = st.file_uploader("Upload resume PDF", type=["pdf"])

resume_data = None

if uploaded_file:
    with st.spinner("Parsing resume..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(
            f"{API_BASE}/resume/upload",
            files={"file": uploaded_file}
        )
        if response.status_code == 200:
            resume_data = response.json()
            st.success("Resume parsed successfully!")
            st.json(resume_data)
        else:
            st.error("Failed to parse resume")

# Job Description
st.header("📝 Job Description")
job_description = st.text_area(
    "Paste job description here",
    height=150
)

# Match Button
if st.button("🔍 Match Resume"):
    if not resume_data or not job_description:
        st.warning("Please upload a resume and enter a job description.")
    else:
        with st.spinner("Matching resume..."):
            payload = {
                "job_description": job_description,
                "resume": resume_data
            }
            match_response = requests.post(
                f"{API_BASE}/match",
                json=payload
            )

            if match_response.status_code == 200:
                result = match_response.json()
                st.success("Match completed!")
                st.subheader("📊 Match Result")
                st.write(f"**Vector Distance:** {result['vector_distance']}")
                st.write("### 🧠 AI Explanation")
                st.write(result["explanation"])
            else:
                st.error("Matching failed")
