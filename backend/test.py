from processor import extract_skills, extract_sections, clean_text
from parser import parse_resume

res = parse_resume("uploads/Mick Enev - Resume.pdf", "NEWOUTPUT.txt")
clean_res = clean_text("NEWOUTPUT.txt", "asdas.txt")
sections = extract_sections("asdas.txt")

print(extract_skills(sections))
