from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def compare_requirements(skills, job_desc):
    with open(job_desc, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = "\n".join(lines)
    prompt = "Based on my skills: " + str(skills) + " and the skills saught after in this job description: " + lines + " would I be a good fit for this role? If not what can I work on to be a good fit?"
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text