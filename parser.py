import pymupdf

def parse_resume(pdf, output):
    doc = pymupdf.open(pdf)
    out = output

    for page in doc: 
        text = page.get_text().encode("utf-8")
        out.write(text)
        out.write(bytes((12,)))
    out.close


# TODO: Implement job description parsing

def parse_job_desc(file_path, output):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))