import pymupdf4llm

def extract_text(filepath):
    with open(filepath, "rb") as file:
        text = pymupdf4llm.to_markdown(file)
    return text