from parser import parse_resume, parse_job_desc
from processor import clean_text, extract_sections, extract_skills, extract_desired_skills
from llm import compare_requirements


def compare_skills():
    parse_job_desc("job-desc.txt", "job-output.txt")

    clean_text("job-output.txt", "clean-job-output.txt")

    extract_desired_skills("clean-job-output.txt")


    sections = extract_sections('output3.txt')

    return compare_requirements(extract_skills(sections), "job-desc.txt")
