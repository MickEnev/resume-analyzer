from parser import parse_resume
from processor import clean_text, extract_sections

out = open("output2.txt", "wb")
parse_resume("Mick Enev - Resume.pdf", out)

clean_text("output.txt", "output3.txt")

out.close()

extract_sections('output3.txt')
