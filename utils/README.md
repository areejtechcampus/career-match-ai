# 🤖 AI Job Matcher Agent

An Agentic AI application that automatically matches a candidate's CV with multiple job opportunities extracted from QR codes.

The system reads the candidate's CV, scans QR code images containing job links, scrapes job descriptions from the web, compares each job with the CV using a Large Language Model (LLM), and generates a ranked Excel report with AI-powered recommendations.

---

## 🚀 Features

* 📄 Upload a CV (PDF)
* 📷 Upload one or multiple QR Code images
* 🔍 Automatically extract job links
* 🌐 Scrape job descriptions
* 🤖 AI-powered job matching using GPT
* 📊 Compatibility score (0–100)
* ✅ Strengths analysis
* ❌ Missing skills detection
* 💡 Personalized recommendations
* 📥 Download Excel report
* 📈 Interactive Streamlit dashboard

---

## 🏗 Project Structure

```
AI_JOB_MATCHER/

│
├── app.py
│
├── Pages/
│   ├── 1_Upload.py
│   ├── 2_Analysis.py
│   └── 3_Dashboard.py
│
├── Utils/
│   ├── barcode.py
│   ├── cv_reader.py
│   ├── scraper.py
│   ├── matcher.py
│   └── report.py
│
├── uploads/
├── outputs/
├── requirements.txt
└── README.md
```

---

## ⚙️ Technologies

* Python
* Streamlit
* LangChain
* OpenAI / OpenRouter
* BeautifulSoup
* PyMuPDF
* Pyzbar
* Pillow
* Pandas

---

## 🧠 Workflow

```
Upload CV
      ↓
Extract PDF Text
      ↓
Upload QR Images
      ↓
Extract URLs
      ↓
Scrape Job Descriptions
      ↓
LLM Job Matching
      ↓
Generate Excel Report
      ↓
Interactive Dashboard
```

---

## 📊 Output

The generated report includes:

* Job Title
* Match Score
* Strengths
* Missing Skills
* Recommendation
* Summary
* Job URL

---

## ▶️ Run the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 📸 Application Screens

* Home Page
* Upload CV
* Upload QR Codes
* AI Analysis
* Dashboard
* Excel Report

---

## 🎯 Future Improvements

* ATS Score Prediction
* Semantic Embeddings Matching
* Support for DOCX CVs
* Job Filtering by Location
* Multi-language Support
* Resume Improvement Suggestions
* Cover Letter Generator
* AI Interview Preparation

---

## 👩‍💻 Author

Developed as an Agentic AI Capstone Project.

Created by **AREEJ ALZAIDI**.
