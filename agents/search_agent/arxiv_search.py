import arxiv
from datetime import datetime
from core.schemas import Paper


def search_arxiv(
    topic: str,
    author: str = None,
    start_date: str = None,
    end_date: str = None,
    max_results: int = 10,
):

    print("Searching arXiv...")
    print("Topic:", topic)

    client = arxiv.Client()

    search = arxiv.Search(
        query=topic,
        max_results=max_results
    )

    papers = []

    try:
        for result in client.results(search):

            authors = [a.name for a in result.authors]
            paper_date = result.published.date()

            # -------------------------
            # Optional Author Filter
            # -------------------------
            if author and author.strip():
                if not any(author.lower() in a.lower() for a in authors):
                    continue

            # -------------------------
            # Optional Start Date
            # -------------------------
            if start_date:
                start = datetime.strptime(start_date, "%Y-%m-%d").date()
                if paper_date < start:
                    continue

            # -------------------------
            # Optional End Date
            # -------------------------
            if end_date:
                end = datetime.strptime(end_date, "%Y-%m-%d").date()
                if paper_date > end:
                    continue

            print("FOUND:", result.title)

            papers.append(
                Paper(
                    title=result.title,
                    authors=authors,
                    summary=result.summary,
                    published=str(paper_date),
                    pdf_url=result.pdf_url,
                    source="arXiv"
                )
            )

    except Exception as e:
        print("arXiv Error:", e)

    print("Total arXiv papers:", len(papers))

    return papers