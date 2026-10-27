import streamlit as st

st.set_page_config(
    page_title="CareerMatch AI",
    page_icon="🚀",
    layout="wide"
)

# ===========================
# Hero
# ===========================

st.title("🚀 CareerMatch AI")

st.subheader(
    "Your Intelligent Career Matching Assistant"
)

st.markdown("""
Analyze your CV against multiple jobs in seconds.

✔ Upload your CV

✔ Upload QR Codes

✔ AI analyzes every job

✔ Get ATS Compatibility Score

✔ Download Excel Report
""")
st.divider()

# ===========================
# Features
# ===========================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        label="CV Format",
        value="PDF"
    )

with c2:
    st.metric(
        label="QR Images",
        value="Unlimited"
    )

with c3:
    st.metric(
        label="AI Engine",
        value="GPT"
    )

with c4:
    st.metric(
        label="Output",
        value="Excel Report"
    )

st.divider()

# ===========================
# Workflow
# ===========================

st.subheader("🚀 Workflow")

st.markdown("""
1. Upload your CV

2. Upload one or more QR Code images

3. Click **Analyze Jobs**

4. AI compares every job with your CV

5. Jobs are ranked from highest to lowest match

6. Download the Excel report
""")

st.divider()

# ===========================
# Sidebar Guide
# ===========================

st.success("""
Use the sidebar to navigate through the application.

📄 Upload Files

🤖 Analyze Jobs

📊 Dashboard
""")

st.divider()

st.caption("AI Job Matcher Agent | Agentic AI Capstone Project")
