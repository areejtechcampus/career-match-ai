import time
from langchain_openai import ChatOpenAI


def match_jobs(cv_text, jobs, api_key):

    llm = ChatOpenAI(
        model="openai/gpt-4o-mini",
        openai_api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=0,
        max_tokens=300
    )

    reports = []

    total_jobs = len(jobs)

    for i, job in enumerate(jobs):

        print(f"Analyzing Job {i+1}/{total_jobs}")

        prompt = f"""
You are an expert AI Recruitment Assistant.

Compare the candidate CV with the job description.

Return ONLY exactly in this format.

Score: integer from 0 to 100

Job Title:

Strengths:

Missing Skills:

Top Skills To Learn:

Recommendation:

Why this score:

Summary:

-------------------------

Candidate CV

{cv_text[:2000]}

-------------------------

Job Description

{job["content"][:1500]}

Do not use markdown.
Do not add explanations.
"""

        try:

            response = llm.invoke(prompt)

            text = response.content

            score = ""
            title = ""
            strengths = ""
            missing = ""
            learn = ""
            recommendation = ""
            why = ""
            summary = ""

            for line in text.split("\n"):

                line = line.strip()

                if line.startswith("Score:"):
                    score = line.replace("Score:", "").strip()

                elif line.startswith("Job Title:"):
                    title = line.replace("Job Title:", "").strip()

                elif line.startswith("Strengths:"):
                    strengths = line.replace("Strengths:", "").strip()

                elif line.startswith("Missing Skills:"):
                    missing = line.replace("Missing Skills:", "").strip()

                elif line.startswith("Top Skills To Learn:"):
                    learn = line.replace(
                        "Top Skills To Learn:",
                        ""
                    ).strip()

                elif line.startswith("Recommendation:"):
                    recommendation = line.replace(
                        "Recommendation:",
                        ""
                    ).strip()

                elif line.startswith("Why this score:"):
                    why = line.replace(
                        "Why this score:",
                        ""
                    ).strip()

                elif line.startswith("Summary:"):
                    summary = line.replace(
                        "Summary:",
                        ""
                    ).strip()

            # -----------------------------
            # Convert score
            # -----------------------------

            try:
                score_num = int(float(score))

            except:
                score_num = 0

            # -----------------------------
            # Match Level
            # -----------------------------

            if score_num >= 90:
                match = "🟢 Excellent Match"

            elif score_num >= 80:
                match = "🔵 Strong Match"

            elif score_num >= 70:
                match = "🟡 Good Match"

            elif score_num >= 60:
                match = "🟠 Fair Match"

            else:
                match = "🔴 Weak Match"

            # -----------------------------
            # Save Result
            # -----------------------------

            reports.append({

                "url": job["url"],

                "job_title": title,

                "score": score_num,

                "match": match,

                "strengths": strengths,

                "missing_skills": missing,

                "skills_to_learn": learn,

                "recommendation": recommendation,

                "why": why,

                "summary": summary

            })

            time.sleep(1)

        except Exception as e:

          raise Exception(e)

    # -----------------------------
    # Sort Jobs
    # -----------------------------

    reports = sorted(

        reports,

        key=lambda x: x["score"],

        reverse=True

    )

    return reports