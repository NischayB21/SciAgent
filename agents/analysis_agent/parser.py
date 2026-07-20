"""
parser.py

Extract text from PDF files using PyMuPDF.
"""

import fitz  # PyMuPDF


def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF.

    Args:
        pdf_path (str): Path to the PDF.

    Returns:
        str: Extracted text.
    """
    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return text