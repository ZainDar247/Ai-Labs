from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)  # For undirected graph
    
    def display(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')

g = Graph()
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)


g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(4, 1)
g.add_edge(4, 3)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(1, 3)

g.display()