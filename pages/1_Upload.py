import streamlit as st

st.set_page_config(
    page_title="Upload Files",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Upload CV & QR Codes")

st.write("Upload your CV and one or more QR code images.")

# ==========================
# Upload CV
# ==========================

cv_file = st.file_uploader(
    "Upload your CV (PDF)",
    type=["pdf"]
)

# ==========================
# Upload QR Images
# ==========================

qr_files = st.file_uploader(
    "Upload QR Images",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

# ==========================
# API Key
# ==========================



st.divider()

# ==========================
# Save
# ==========================

if st.button("Save Files"):

    if cv_file is None:
        st.error("Please upload your CV.")
        st.stop()

    if len(qr_files) == 0:
        st.error("Please upload QR images.")
        st.stop()

   

    st.session_state["cv_file"] = cv_file
    st.session_state["qr_files"] = qr_files
    

    st.success("Files uploaded successfully!")

    st.info("➡️ Go to the Analysis page.")