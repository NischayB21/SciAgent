"""
recommendation_agent.py

Generates research recommendations based on
paper analysis and identified research gaps.
"""

import json
from ollama import chat


SYSTEM_PROMPT = """
You are an AI research advisor.

You will receive:
1. A structured analysis of a research paper.
2. The identified research gaps.

Suggest:

- Novel research ideas
- Possible improvements
- Future project directions

Return ONLY valid JSON.

Schema:

{
    "research_ideas": ["string"],
    "improvements": ["string"],
    "future_projects": ["string"]
}
"""


class RecommendationAgent:

    def recommend(self, analysis: dict, gaps: dict):

        payload = {
            "analysis": analysis,
            "gaps": gaps
        }

        response = chat(
            model="qwen2.5:7b",
            format="json",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": json.dumps(payload, indent=2)
                }
            ]
        )

        data = json.loads(response["message"]["content"])

        return {
            "research_ideas": data.get("research_ideas", []),
            "improvements": data.get("improvements", []),
            "future_projects": data.get("future_projects", [])
        }


recommendation_agent = RecommendationAgent()