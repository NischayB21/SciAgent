"""
graph_builder.py

Builds a simple knowledge graph from analyzed research papers.
"""

import networkx as nx


class KnowledgeGraph:

    def __init__(self):
        self.graph = nx.Graph()

    def add_paper(self, title: str, methods: list, datasets: list):

        # Add paper node
        self.graph.add_node(title, type="Paper")

        # Connect methods
        for method in methods:
            self.graph.add_node(method, type="Method")
            self.graph.add_edge(title, method)

        # Connect datasets
        for dataset in datasets:
            self.graph.add_node(dataset, type="Dataset")
            self.graph.add_edge(title, dataset)

    def get_nodes(self):
        return list(self.graph.nodes(data=True))

    def get_edges(self):
        return list(self.graph.edges())


knowledge_graph = KnowledgeGraph()