import streamlit as st
from resume_parser import extract_text
from job_matcher import get_job_fit_score_and_roles

st.title("🧠 AI Resume Screener")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file:
    with open("resumes/temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text("resumes/temp_resume.pdf")
    job_role = st.selectbox("Select a job role", ["Software Engineer", "Data Analyst"])

    if st.button("Analyze Resume"):
        score, suggestions = get_job_fit_score_and_roles(resume_text, job_role)
        st.success(f"Job Fit Score: {score}/100")
        st.info("Suggested Roles:")
        for role in suggestions:
            st.write(f"- {role}")
