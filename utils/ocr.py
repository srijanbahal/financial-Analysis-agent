import pytesseract
from pdf2image import convert_from_bytes

def extract_text_from_pdf(pdf_bytes):
    images = convert_from_bytes(pdf_bytes)
    text = ""
    for img in images:
        text += pytesseract.image_to_string(img)
    return text
