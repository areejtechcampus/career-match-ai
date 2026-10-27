import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="AI Job Matcher Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================
# CSS
# ==========================

st.markdown("""
<style>

.stApp{
    background:#f5f7fb;
}

.card{
    background:white;
    border-radius:18px;
    padding:25px;
    margin-bottom:25px;
    box-shadow:0px 5px 18px rgba(0,0,0,.08);
}

.progress{
    background:#e5e7eb;
    height:18px;
    border-radius:20px;
    overflow:hidden;
    margin-top:8px;
    margin-bottom:15px;
}

.bar{
    height:18px;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

st.title("📊 AI Job Matching Dashboard")

# ==========================
# Check report
# ==========================

if "report_df" not in st.session_state:

    st.warning("Please run the analysis first.")

    st.stop()

report_df = st.session_state["report_df"]

report_df["score"] = pd.to_numeric(
    report_df["score"],
    errors="coerce"
)

# ==========================
# Match Label
# ==========================

def get_match(score):

    if score >= 90:
        return "🟢 Excellent Match"

    elif score >= 80:
        return "🔵 Strong Match"

    elif score >= 70:
        return "🟡 Good Match"

    elif score >= 60:
        return "🟠 Fair Match"

    else:
        return "🔴 Weak Match"

report_df["match"] = report_df["score"].apply(get_match)

# ==========================
# Metrics
# ==========================

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Jobs",
        len(report_df)
    )

with c2:
    st.metric(
        "Best Score",
        f"{report_df['score'].max():.0f}%"
    )

with c3:
    st.metric(
        "Average Score",
        f"{report_df['score'].mean():.1f}%"
    )

st.divider()

# ==========================
# Cards
# ==========================

for _, row in report_df.iterrows():

    score = int(row["score"])

    if score >= 90:
        color = "#22c55e"

    elif score >= 80:
        color = "#2563eb"

    elif score >= 70:
        color = "#f59e0b"

    else:
        color = "#ef4444"

    st.markdown(f"""
    <div class="card">

    <h2>💼 {row['job_title']}</h2>

    <h3 style="color:{color};">
    {row['match']}
    </h3>

    <div class="progress">

        <div
        class="bar"
        style="
        width:{score}%;
        background:{color};
        ">
        </div>

    </div>

    <h2>{score}%</h2>

    <hr>

    <h4>✅ Strengths</h4>

    <p>{row['strengths']}</p>

    <h4>❌ Missing Skills</h4>

    <p>{row['missing_skills']}</p>

    <h4>💡 Recommendation</h4>

    <p>{row['recommendation']}</p>

    <h4>📝 Summary</h4>

    <p>{row['summary']}</p>

    </div>

    """, unsafe_allow_html=True)

    st.link_button(
        "🔗 View Job",
        row["url"],
        use_container_width=True
    )

    st.divider()

# ==========================
# Download Report
# ==========================

report_path = os.path.join(
    "outputs",
    "Job_Analysis_Report.xlsx"
)

if os.path.exists(report_path):

    with open(report_path, "rb") as f:

        st.download_button(
            "📥 Download Excel Report",
            data=f,
            file_name="Job_Analysis_Report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )