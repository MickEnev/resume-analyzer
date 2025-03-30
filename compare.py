from parser import parse_resume, parse_job_desc
from processor import clean_text, extract_sections, extract_skills, extract_desired_skills
from llm import compare_requirements


def compare_skills(resume, jobDesc):
    # Parse resume into a text file
    parse_resume(resume, "Parsed-Resume.txt")
    # Clean text by removing any white space, non-alphanumeric characters (except for +'s), and changing to all lower case
    clean_text("Parsed-Resume.txt", "Clean-Parsed_Resume.txt")
    # Group resume text by section
    sections = extract_sections("Clean-Parsed_Resume.txt")
    # Extract relevant skills form sections
    skills = extract_skills(sections)
    return compare_requirements(skills, jobDesc)
