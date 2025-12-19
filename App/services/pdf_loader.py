import fitz


def extract_resume_text(pdf_path:str)->str:
    doc=fitz.open(pdf_path)
    for page in doc:
        text=""
        text=text+page.get_text()
    return text

