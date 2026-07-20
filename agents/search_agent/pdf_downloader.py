"""
pdf_downloader.py

Downloads research paper PDFs and saves them locally.
"""

import os
import re
import requests


class PDFDownloader:
    """Downloads PDF files from research paper URLs."""

    def __init__(self):
        self.save_dir = "data/papers"
        os.makedirs(self.save_dir, exist_ok=True)

    def _safe_filename(self, filename: str) -> str:
        """Remove invalid filename characters."""
        filename = re.sub(r'[<>:"/\\|?*]', "_", filename)
        filename = filename.strip()

        if not filename.endswith(".pdf"):
            filename += ".pdf"

        return filename

    def download_pdf(self, pdf_url: str, filename: str) -> str:
        """
        Download a PDF and return the local file path.
        """

        filename = self._safe_filename(filename)
        file_path = os.path.join(self.save_dir, filename)

        # Skip download if already exists
        if os.path.exists(file_path):
            print(f"PDF already exists: {file_path}")
            return file_path

        print(f"Downloading: {pdf_url}")

        response = requests.get(
            pdf_url,
            timeout=60,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        with open(file_path, "wb") as pdf_file:
            pdf_file.write(response.content)

        print(f"Saved: {file_path}")

        return file_path


pdf_downloader = PDFDownloader()


def download_pdf(pdf_url: str, filename: str) -> str:
    """
    Convenience wrapper.
    """
    return pdf_downloader.download_pdf(pdf_url, filename)