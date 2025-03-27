from parser import parse_resume, parse_job_desc
from processor import clean_text, extract_sections, extract_skills, extract_desired_skills


parse_job_desc("job-desc.txt", "job-output.txt")

clean_text("job-output.txt", "clean-job-output.txt")

print(extract_desired_skills("clean-job-output.txt"))

'''clean_text("output.txt", "output3.txt")



sections = extract_sections('output3.txt')

sections['education']

print(extract_skills(sections))
'''