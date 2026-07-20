"""
download_agent.py

Downloads research paper PDFs.
"""

import os
import requests

from core.schemas import Paper


class DownloadAgent:

    def __init__(self):
        self.download_dir = "data/papers"
        os.makedirs(self.download_dir, exist_ok=True)

    def download(self, paper: Paper) -> str:

        if not paper.pdf_url:
            raise Exception(f"No PDF URL found for '{paper.title}'")

        output_path = os.path.join(
            self.download_dir,
            "current.pdf"
        )

        print("=" * 60)
        print("DOWNLOAD AGENT")
        print("=" * 60)
        print("Title:", paper.title)
        print("Downloading:", paper.pdf_url)

        response = requests.get(
            paper.pdf_url,
            timeout=60
        )

        response.raise_for_status()

        with open(output_path, "wb") as file:
            file.write(response.content)

        print("Saved:", output_path)
        print("=" * 60)

        return output_path


download_agent = DownloadAgent()