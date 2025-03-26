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