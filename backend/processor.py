import re

def clean_text(file_path, output_path):
    # Remove bullets
    # Remove unnecessary whitespace
    # Convert text to lower case
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    cleaned_lines = []
    for line in lines:
        line = re.sub(r'[^a-zA-Z0-9.,\-\s+]', '', line)  # Remove special characters
        line = re.sub(r'\s+', ' ', line)  # Replace multiple spaces/newlines with a single space
        line = line.lower().strip()  # Convert to lowercase and remove leading/trailing spaces
        cleaned_lines.append(line)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(cleaned_lines))


def extract_sections(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

    sections = {
        'experience': [],
        'skills': [], 
        'education': [], 
        'projects': []
    }
    

    current_section = None

    for line in lines:
        if line in sections:
            current_section = line
        elif current_section:
            sections[current_section].append(line)
    return sections


def extract_skills(sections):
    # TODO: Curate a full list of relevant SWE skills
    skill_keywords = {"python", "c++", "java", "react", "javascript", "sql", "aws", "docker", "tensorflow", "machine learning", "data visualization", "git", "node.js", "github", "urbana-champaign", "bachelor's degree", "master's degree", "computer science", "software engineering",
                    "c", "2024", "2025"}
    found_skills = set()
    for section in sections.values():
        for words in section:
            skills = words.split()
            for skill in skills:
                skill = re.sub(r"^[^a-zA-Z+-]+|[^a-zA-Z+-]+$", "", skill)
                if skill in skill_keywords:
                    found_skills.add(skill)
    
    return found_skills

def extract_desired_skills(file_path):
    # TODO: Curate a full list of relevant SWE skills
    skill_keywords = {"python", "c++", "java", "react", "javascript", "sql", "aws", "docker", "tensorflow", "machine learning", "data visualization", "git", "node.js", "github", "urbana-champaign", "bachelor's degree", "master's degree", "computer science", "software engineering",
                    "c", "2024", "2025"}
    found_skills = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        words = line.split()
        for word in words:
            
            word = re.sub(r"^[^a-zA-Z+-]+|[^a-zA-Z+-]+$", "", word)
            if word in skill_keywords:
                found_skills.add(word)
    return found_skills
    
