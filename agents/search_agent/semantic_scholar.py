import requests
from datetime import datetime

from core.schemas import Paper

BASE_URL = "https://api.semanticscholar.org/graph/v1/paper/search"


def search_semantic_scholar(
    topic: str,
    author: str = None,
    start_date: str = None,
    end_date: str = None,
    limit: int = 10
):

    params = {
        "query": topic,
        "limit": limit,
        "fields": "title,authors,abstract,year,openAccessPdf"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()

    except requests.RequestException as e:
        print("Semantic Scholar Error:", e)
        return []

    data = response.json()

    papers = []

    for item in data.get("data", []):

        authors = [
            a.get("name", "")
            for a in item.get("authors", [])
        ]

        # -----------------------------
        # Author Filter
        # -----------------------------
        if author:
            if not any(author.lower() in a.lower() for a in authors):
                continue

        # -----------------------------
        # Date Filter
        # -----------------------------
        year = item.get("year")

        if year:

            paper_date = datetime(
                int(year),
                1,
                1
            ).date()

            if start_date:
                start = datetime.strptime(
                    start_date,
                    "%Y-%m-%d"
                ).date()

                if paper_date < start:
                    continue

            if end_date:
                end = datetime.strptime(
                    end_date,
                    "%Y-%m-%d"
                ).date()

                if paper_date > end:
                    continue

        papers.append(
            Paper(
                title=item.get("title", ""),
                authors=authors,
                summary=item.get("abstract", ""),
                published=str(year),
                pdf_url=item.get("openAccessPdf", {}).get("url", ""),
                source="Semantic Scholar"
            )
        )

    return papers