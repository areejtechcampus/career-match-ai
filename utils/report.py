import os
import pandas as pd


def create_report(results):

    if len(results) == 0:
        return pd.DataFrame()

    report_df = pd.DataFrame(results)

    report_df["score"] = pd.to_numeric(
        report_df["score"],
        errors="coerce"
    )

    report_df = report_df.sort_values(
        by="score",
        ascending=False
    )

    # ترتيب الأعمدة
    columns = [
        "job_title",
        "score",
        "match",
        "strengths",
        "missing_skills",
        "skills_to_learn",
        "recommendation",
        "why",
        "summary",
        "url"
    ]

    # الاحتفاظ فقط بالأعمدة الموجودة
    report_df = report_df[[c for c in columns if c in report_df.columns]]

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    report_path = os.path.join(
        "outputs",
        "Job_Analysis_Report.xlsx"
    )

    report_df.to_excel(
        report_path,
        index=False
    )

    return report_df