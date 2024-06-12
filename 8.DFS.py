class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append((u, weight))  # Assuming it's an undirected graph

    def dfs_shortest_path(self, start, goal):
        visited = set()
        min_cost, best_path = self._dfs_helper(start, goal, visited, path=[], total_cost=0, min_cost=float('inf'), best_path=[])
        return best_path, min_cost

    def _dfs_helper(self, node, goal, visited, path, total_cost, min_cost, best_path):
        visited.add(node)
        path.append(node)

        if node == goal:
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path.copy()
        else:
            for neighbor, cost in self.graph[node]:
                if neighbor not in visited:
                    min_cost, best_path = self._dfs_helper(neighbor, goal, visited, path, total_cost + cost, min_cost, best_path)

        path.pop()
        visited.remove(node)

        return min_cost, best_path

# Example usage
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'D', 2)
g.add_edge('B', 'E', 5)
g.add_edge('C', 'F', 3)
g.add_edge('E', 'F', 1)

start = 'A'
goal = 'F'
best_path, min_cost = g.dfs_shortest_path(start, goal)

if best_path:
    print(f"Shortest path found: {' -> '.join(best_path)} with total cost: {min_cost}")
else:
    print("No path found.")
