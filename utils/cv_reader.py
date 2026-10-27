import fitz
import tempfile
import os


def extract_cv_text(uploaded_pdf):
    """
    Extract text from uploaded PDF CV.
    """

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

        tmp.write(uploaded_pdf.read())

        pdf_path = tmp.name

    text = ""

    try:

        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()

    except Exception as e:

        print(f"PDF Error: {e}")

    finally:

        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    return text