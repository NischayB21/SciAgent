"""
gap_agent.py

Identifies research gaps from analyzed papers.
"""

from ollama import chat
import json


SYSTEM_PROMPT = """
You are an AI research assistant.

Analyze the extracted information from a research paper.

Identify:

1. Research gaps
2. Future work
3. Open challenges

Return ONLY valid JSON.

Schema:

{
    "research_gaps": ["string"],
    "future_work": ["string"],
    "open_challenges": ["string"]
}
"""


class GapAgent:

    def analyze(self, analysis: dict):

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
                    "content": json.dumps(analysis, indent=2)
                }
            ]
        )

        data = json.loads(response["message"]["content"])

        return {
            "research_gaps": data.get("research_gaps", []),
            "future_work": data.get("future_work", []),
            "open_challenges": data.get("open_challenges", [])
        }


gap_agent = GapAgent()