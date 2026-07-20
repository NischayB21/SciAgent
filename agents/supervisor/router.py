from .state import AgentState


class Router:

    def get_next_agent(self, state: AgentState):
        if not state.agent_sequence:
            return "search_agent"
        return state.agent_sequence[-1]