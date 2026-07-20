"""
knowledge_agent.py

Stores analyzed paper information in the knowledge graph.
"""

from agents.knowledge_agent.graph_builder import knowledge_graph


class KnowledgeAgent:
    """Stores structured paper analysis."""

    def process(self, analysis: dict) -> dict:
        """
        Store extracted information into the knowledge graph.
        """

        knowledge_graph.add_paper(
            title=analysis["title"],
            methods=analysis["methods"],
            datasets=analysis["datasets"]
        )

        return {
            "status": "success",
            "paper": analysis["title"],
            "summary": analysis["summary"],
            "methods": analysis["methods"],
            "datasets": analysis["datasets"],
            "metrics": analysis["metrics"],
            "limitations": analysis["limitations"]
        }


knowledge_agent = KnowledgeAgent()