import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👩‍💻",
    layout="centered"
)

st.title("👩‍💻 About the Developer")

st.markdown("""
## Areej Alzaidi

AI & Machine Learning Developer

This project uses Artificial Intelligence to:

- 📄 Analyze CVs
- 📷 Scan QR Codes
- 🌐 Extract Job Descriptions
- 🤖 Match Jobs using LLMs
- 📊 Rank opportunities automatically
""")

st.link_button(
    "🐙 GitHub",
    "https://github.com/areejtechcampus"
)

st.link_button(
    "💼 LinkedIn",
    "https://www.linkedin.com/in/areej-alzaidi/"
)

st.markdown("---")
st.caption("© 2026 Areej Alzaidi")