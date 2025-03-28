from flask import Flask
import time
from processor import clean_text, extract_sections, extract_skills, extract_desired_skills
from compare import compare_skills

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index</p>"

@app.route("/time")
def get_time():
    return {'time': time.time()}

@app.route("/skills")
def get_skills():
    skills = compare_skills()
    return {'skills': skills} if isinstance(skills, (str, list, dict)) else {'error': 'Invalid response'}