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
    print(sections)
    return sections


def extract_skills(text):
    temp = 0