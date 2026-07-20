"""
openalex.py

Search papers from OpenAlex.
Supports optional author and date filtering.
"""

import requests
from datetime import datetime
from core.schemas import Paper

BASE_URL = "https://api.openalex.org/works"


def search_openalex(
    topic: str,
    author: str = None,
    start_date: str = None,
    end_date: str = None,
    limit: int = 10,
):

    print("=" * 50)
    print("Searching OpenAlex...")
    print("Topic:", topic)

    params = {
        "search": topic,
        "per-page": limit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print("OpenAlex Error:", e)
        return []

    data = response.json()

    print("Results received:", len(data.get("results", [])))

    papers = []

    for work in data.get("results", []):

        title = work.get("display_name", "")

        authors = [
            item.get("author", {}).get("display_name", "")
            for item in work.get("authorships", [])
        ]

        publication_year = work.get("publication_year")

        # -------------------------
        # Optional Author Filter
        # -------------------------
        if author and author.strip():
            if not any(author.lower() in a.lower() for a in authors):
                continue

        # -------------------------
        # Optional Date Filter
        # -------------------------
        if publication_year:

            paper_date = datetime(
                int(publication_year),
                1,
                1
            ).date()

            if start_date and start_date.strip():
                start = datetime.strptime(
                    start_date,
                    "%Y-%m-%d"
                ).date()

                if paper_date < start:
                    continue

            if end_date and end_date.strip():
                end = datetime.strptime(
                    end_date,
                    "%Y-%m-%d"
                ).date()

                if paper_date > end:
                    continue

        paper = Paper(
            title=title,
            authors=authors,
            summary="",
            published=str(publication_year),
            pdf_url=(
                work.get("primary_location", {}).get("pdf_url")
                or ""
            ),
            source="OpenAlex"
        )

        papers.append(paper)

    print("OpenAlex returned", len(papers), "papers")

    for paper in papers:
        print("OA:", paper.title)

    print("=" * 50)

    return papers