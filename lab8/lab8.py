import heapq

class Node:
    def __init__(self, name, heuristic=0):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = []
        self.g_cost = float('inf')  # Cost to reach this node from the start node
        self.parent = None

    def add_neighbor(self, neighbor, cost):
        self.neighbors.append((neighbor, cost))

    def __lt__(self, other):
        return (self.g_cost + self.heuristic) < (other.g_cost + other.heuristic)

def a_star_search(start_node, goal_node):
    open_list = []
    heapq.heappush(open_list, (start_node.heuristic, start_node))
    start_node.g_cost = 0
    came_from = {}
    
    while open_list:
        _, current_node = heapq.heappop(open_list)
        
        if current_node == goal_node:
            return reconstruct_path(came_from, goal_node)
        
        for neighbor, cost in current_node.neighbors:
            tentative_g_cost = current_node.g_cost + cost
            if tentative_g_cost < neighbor.g_cost:
                neighbor.g_cost = tentative_g_cost
                neighbor.parent = current_node
                came_from[neighbor] = current_node
                if neighbor not in open_list:
                    heapq.heappush(open_list, (neighbor.g_cost + neighbor.heuristic, neighbor))
    
    return None

def reconstruct_path(came_from, goal_node):
    path = []
    while goal_node:
        path.append(goal_node.name)
        goal_node = came_from.get(goal_node)
    return path[::-1]

# Example usage
if __name__ == "__main__":
    # Create nodes with heuristic values
    a = Node('A', 6)
    b = Node('B', 5)
    c = Node('C', 4)
    d = Node('D', 3)
    e = Node('E', 2)
    f = Node('F', 0)
    
    # Define neighbors
    a.add_neighbor(b, 1)
    a.add_neighbor(c, 4)
    b.add_neighbor(d, 2)
    c.add_neighbor(d, 1)
    d.add_neighbor(e, 5)
    e.add_neighbor(f, 1)

    # Perform A* Search
    path = a_star_search(a, f)
    print("Path:", path)
