import itertools
import networkx as nx
import matplotlib.pyplot as plt

def tsp_brute_force(graph):
    cities = list(graph.keys())
    min_path, min_cost = None, float('inf')
    
    for perm in itertools.permutations(cities):
        cost = sum(graph[perm[i]][perm[i+1]] for i in range(len(perm) - 1))
        cost += graph[perm[-1]][perm[0]]
        if cost < min_cost:
            min_cost, min_path = cost, perm
    
    return min_path, min_cost

def draw_graph(graph, path):
    G = nx.Graph()
    
    # Add nodes and edges with weights to the graph
    for city, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(city, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)  # positions for all nodes
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    
    # Highlight the path
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)] + [(path[-1], path[0])]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    
    plt.title("TSP Solution Visualization")
    plt.show()

# Example graph represented as a dictionary of dictionaries
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Run the TSP algorithm
shortest_path, min_cost = tsp_brute_force(graph)

print("Shortest Path:", shortest_path)
print("Minimum Cost:", min_cost)

# Draw the graph with the shortest path highlighted
draw_graph(graph, shortest_path)
