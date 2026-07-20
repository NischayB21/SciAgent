"""
llm_extractor.py

Uses a local Ollama LLM to extract structured information
from retrieved RAG context.
"""

import json
import re
from ollama import chat


SYSTEM_PROMPT = """
You are an expert AI research paper analysis assistant.

You will receive excerpts from ONE research paper.

Your task is ONLY to extract structured information.

Return ONLY valid JSON.

DO NOT:
- Explain the paper.
- Continue proofs.
- Answer questions.
- Add markdown.
- Add code fences.
- Add comments.

The JSON MUST ALWAYS contain ALL of these keys:

{
    "summary": "string",
    "methods": ["string"],
    "datasets": ["string"],
    "metrics": ["string"],
    "limitations": ["string"]
}

Rules:

1. ALWAYS include every key.
2. If no datasets exist, return:
   "datasets": []
3. If no metrics exist, return:
   "metrics": []
4. If no limitations exist, return:
   "limitations": []
5. Every list must contain ONLY strings.
6. Do NOT invent information.
7. Return ONLY valid JSON.
"""


def extract_with_llm(context: str):
    """
    Sends the retrieved RAG context to the local Ollama model.
    Makes exactly ONE LLM call.
    """

    print("Calling Ollama...")
    print(f"Context length: {len(context)} characters")

    response = chat(
        model="qwen2.5:7b",
        format="json",  # Force JSON output
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
Extract the following information from the research paper.

Return ONLY valid JSON.

Paper Context:

{context}
"""
            }
        ]
    )

    print("Received response from Ollama.")

    content = response["message"]["content"].strip()

    # Remove markdown fences if the model adds them
    content = re.sub(r"^```json", "", content)
    content = re.sub(r"^```", "", content)
    content = re.sub(r"```$", "", content)
    content = content.strip()

    print("\nLLM Output:\n")
    print(content)
    print()

    try:
        data = json.loads(content)

        return {
            "summary": data.get("summary", ""),
            "methods": sorted(set(data.get("methods", []))),
            "datasets": sorted(set(data.get("datasets", []))),
            "metrics": sorted(set(data.get("metrics", []))),
            "limitations": sorted(set(data.get("limitations", [])))
        }

    except Exception as e:
        print("LLM JSON Parsing Error:", e)

        return {
            "summary": "",
            "methods": [],
            "datasets": [],
            "metrics": [],
            "limitations": []
        }