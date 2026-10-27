import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from utils.cv_reader import extract_cv_text
from utils.barcode import extract_urls
from utils.scraper import scrape_jobs
from utils.matcher import match_jobs
from utils.report import create_report

st.set_page_config(
    page_title="Analysis",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Job Analysis")

# ===========================
# Check uploaded files
# ===========================

if "cv_file" not in st.session_state or "qr_files" not in st.session_state:

    st.warning("Please upload your CV and QR images first.")

    st.stop()

cv_file = st.session_state["cv_file"]
qr_files = st.session_state["qr_files"]

api_key = st.secrets["OPENROUTER_API_KEY"]

# ===========================
# Run Analysis
# ===========================

if st.button("🚀 Start AI Analysis", use_container_width=True):

    with st.status("🤖 AI Analysis in Progress...", expanded=True) as status:

        st.write("📄 Reading CV...")
        cv_text = extract_cv_text(cv_file)
        st.success("CV loaded successfully")

        st.write("📷 Scanning QR Codes...")
        urls = extract_urls(qr_files)
        st.success(f"Found {len(urls)} QR Code(s)")
        st.write("URLs:", urls) #

        st.write("🌐 Extracting Job Descriptions...")
        jobs = scrape_jobs(urls)
        st.success(f"Scraped {len(jobs)} Job(s)")
        st.write("Jobs:", jobs) #

        st.write("🤖 Matching Jobs with AI...")
        reports = match_jobs(
            cv_text,
            jobs,
            api_key
        )
        st.success(f"Analyzed {len(reports)} Job(s)")
        st.write("Reports:", reports) #

        st.write("📊 Creating Report...")
        report_df = create_report(reports)

        status.update(
            label="✅ Analysis Completed Successfully!",
            state="complete"
        )

    st.session_state["report_df"] = report_df

    st.toast("Analysis Finished 🎉")

    st.balloons()

    st.dataframe(
        report_df,
        use_container_width=True
    )
    # Debug
    st.write("Columns:")
    st.write(report_df.columns.tolist())

    st.write("Data:")
    st.write(report_df)

    st.dataframe(
        report_df,
        use_container_width=True
    )
