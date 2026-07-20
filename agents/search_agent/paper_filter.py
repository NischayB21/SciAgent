from typing import List
from core.schemas import Paper


def filter_papers(papers: List[Paper]) -> List[Paper]:
    """
    Remove duplicates,
    remove papers without PDFs,
    sort newest first.
    """

    unique = {}

    for paper in papers:

        if not paper.pdf_url:
            continue

        key = paper.title.lower().strip()

        if key not in unique:
            unique[key] = paper

    filtered = list(unique.values())

    filtered.sort(
        key=lambda x: x.published,
        reverse=True
    )

    print("=" * 50)
    print(f"Total papers before filtering : {len(papers)}")
    print(f"Papers with PDFs             : {len(filtered)}")
    print("=" * 50)

    return filtered[:20]