"""
search_agent.py

Main Search Agent.
Searches multiple paper sources and combines results.
"""

from agents.search_agent.arxiv_search import search_arxiv
from agents.search_agent.semantic_scholar import search_semantic_scholar
from agents.search_agent.openalex import search_openalex
from agents.search_agent.paper_filter import filter_papers


class SearchAgent:

    def search(
        self,
        topic: str,
        author: str = None,
        start_date: str = None,
        end_date: str = None,
    ):

        print("=" * 60)
        print("SEARCH AGENT")
        print("=" * 60)

        # -----------------------------
        # arXiv
        # -----------------------------
        print("Searching arXiv...")
        arxiv_results = search_arxiv(
            topic=topic,
            author=author,
            start_date=start_date,
            end_date=end_date
        )
        print(f"arXiv returned {len(arxiv_results)} papers")

        # -----------------------------
        # Semantic Scholar
        # -----------------------------
        print("Searching Semantic Scholar...")
        semantic_results = search_semantic_scholar(
            topic=topic,
            author=author,
            start_date=start_date,
            end_date=end_date
        )
        print(f"Semantic Scholar returned {len(semantic_results)} papers")

        # -----------------------------
        # OpenAlex
        # -----------------------------
        print("Searching OpenAlex...")
        openalex_results = search_openalex(
            topic=topic,
            author=author,
            start_date=start_date,
            end_date=end_date
        )
        print(f"OpenAlex returned {len(openalex_results)} papers")

        # -----------------------------
        # Combine Results
        # -----------------------------
        papers = (
            arxiv_results +
            semantic_results +
            openalex_results
        )

        print(f"Total papers before filtering: {len(papers)}")

        # -----------------------------
        # Remove Duplicates
        # -----------------------------
        papers = filter_papers(papers)

        print(f"Total papers after filtering: {len(papers)}")
        print("=" * 60)

        return papers


search_agent = SearchAgent()