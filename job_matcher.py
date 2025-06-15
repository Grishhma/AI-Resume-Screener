import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_job_fit_score_and_roles(resume_text, job_role):
    prompt = f"""
You are a resume screening assistant.
Resume: {resume_text}
Target Job Role: {job_role}
1. Rate the resume's fit for this role out of 100.
2. Suggest 3 alternative job roles that might suit this candidate.
Respond in JSON: {{ "score": X, "suggested_roles": ["role1", "role2", "role3"] }}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.choices[0].message["content"]
    import json
    parsed = json.loads(content)
    return parsed["score"], parsed["suggested_roles"]
