from typing import List
from core.schemas import Paper


class AgentState:

    def __init__(self, topic: str):
        self.topic = topic
        self.current_agent = "supervisor"
        self.status = "started"
        self.papers: List[Paper] = []
        self.available_agents = ["search_agent"]
        self.agent_sequence = ["supervisor", "search_agent"]