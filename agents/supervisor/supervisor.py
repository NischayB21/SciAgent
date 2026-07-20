"""
supervisor.py

Coordinates the complete SciAgent workflow.
"""

from agents.analysis_agent.analysis_agent import analysis_agent
from agents.knowledge_agent.knowledge_agent import knowledge_agent
from agents.gap_agent.gap_agent import gap_agent
from agents.recommendation_agent.recommendation_agent import recommendation_agent


class Supervisor:

    def process_paper(self, title: str, pdf_path: str):

        print("=" * 80)
        print("STEP 1: ANALYSIS")
        print("=" * 80)

        analysis = analysis_agent.analyze(
            title=title,
            pdf_path=pdf_path
        )

        print("\n" + "=" * 80)
        print("STEP 2: KNOWLEDGE STORAGE")
        print("=" * 80)

        knowledge = knowledge_agent.process(analysis)

        print("\n" + "=" * 80)
        print("STEP 3: GAP ANALYSIS")
        print("=" * 80)

        gaps = gap_agent.analyze(analysis)

        print("\n" + "=" * 80)
        print("STEP 4: RECOMMENDATIONS")
        print("=" * 80)

        recommendations = recommendation_agent.recommend(
            analysis,
            gaps
        )

        return {
            "analysis": analysis,
            "knowledge": knowledge,
            "gaps": gaps,
            "recommendations": recommendations
        }


supervisor = Supervisor()