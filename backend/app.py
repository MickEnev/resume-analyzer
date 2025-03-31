from flask import Flask, request, jsonify
import time
from processor import clean_text, extract_sections, extract_skills
from parser import parse_resume, parse_job_desc
from compare import compare_skills
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/skills", methods=["POST"])
def get_skills():
    if "resume" not in request.files or "job_description" not in request.files:
        return jsonify({"error": "Both resume and job description are required"}), 400
    
    resume = request.files["resume"]
    job_description = request.files["job_description"]

    if resume.filename == "" or job_description.filename == "":
        return jsonify({"error": "Both files must be selected"}), 400

    resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    job_description_path = os.path.join(UPLOAD_FOLDER, job_description.filename)

    resume.save(resume_path)
    job_description.save(job_description_path)

    skills = compare_skills(resume_path, job_description_path)
    
    return {'skills': skills} if isinstance(skills, (str, list, dict)) else {'error': 'Invalid response'}