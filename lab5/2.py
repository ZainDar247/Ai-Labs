from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque(start)
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            if node=="G":
                print("search stopped!!")
                exit(1)
            visited.add(node)
            queue.extend(i for i in graph[node] if i not in visited)
#------------------------------------------------------------------------

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
#------------------------------------------------------------------------

g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('H')
g.add_node('I')
g.add_node('J')
g.add_node('K')
g.add_node('L')
g.add_node('M')
g.add_node('N')

g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('K', 'M')
g.add_edge('K', 'N')
g.add_edge('D', 'G')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('I', 'L')

g.display()

print("Breadth First Search :")
bfs(g.graph, "A")