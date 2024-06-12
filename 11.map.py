class MapColoringCSP:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.coloring = {}

    def is_valid_color(self, region, color):
        for neighbor in self.graph[region]:
            if neighbor in self.coloring and self.coloring[neighbor] == color:
                return False
        return True

    def solve(self, region):
        if region not in self.graph:
            return True
        for color in self.colors:
            if self.is_valid_color(region, color):
                self.coloring[region] = color
                if self.solve(self.get_next_region(region)):
                    return True
                del self.coloring[region]
        return False

    def get_next_region(self, region):
        # This function can be customized to choose the next region to color
        return chr(ord(region) + 1) if region != 'Z' else None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}
colors = ['Red', 'Green', 'Blue']

csp = MapColoringCSP(graph, colors)
csp.solve('A')

print("Region Coloring:")
for region, color in csp.coloring.items():
    print(region, ":", color)
