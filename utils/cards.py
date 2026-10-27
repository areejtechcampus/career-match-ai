import streamlit as st

def show_job_card(row):

    score = int(row["score"])

    if score >= 90:
        color = "#22c55e"
    elif score >= 80:
        color = "#3b82f6"
    elif score >= 70:
        color = "#f59e0b"
    else:
        color = "#ef4444"

    st.markdown(
        f"""
<div style="
background:white;
padding:25px;
border-radius:18px;
box-shadow:0 4px 15px rgba(0,0,0,.08);
margin-bottom:25px;
">

<h2>💼 {row["job_title"]}</h2>

<h4 style="color:{color};">
{row["match"]}
</h4>

<progress
value="{score}"
max="100"
style="
width:100%;
height:20px;
">
</progress>

<h2>{score}%</h2>

<hr>

<h4>✅ Strengths</h4>

<p>{row["strengths"]}</p>

<h4>❌ Missing Skills</h4>

<p>{row["missing_skills"]}</p>

<h4>💡 Recommendation</h4>

<p>{row["recommendation"]}</p>

<a href="{row["url"]}" target="_blank">

🔗 View Job

</a>

</div>
""",
unsafe_allow_html=True
)