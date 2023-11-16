from collections import defaultdict

def find_eulerian_path(graph):
    def dfs(vertex):
        nonlocal eulerian_path
        if vertex in graph:
            neighbors = graph[vertex]
            for neighbor in neighbors:
                if (vertex, neighbor) not in visited_edges:
                    visited_edges.add((vertex, neighbor))
                    dfs(neighbor)
                    eulerian_path.insert(0, neighbor)

    eulerian_path = []
    visited_edges = set()

    # Count the in-degree and out-degree of each vertex
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for vertex, neighbors in graph.items():
        out_degree[vertex] += len(neighbors)
        for neighbor in neighbors:
            in_degree[neighbor] += 1
            out_degree[neighbor] -= 1

    # Find a starting vertex with out-degree > 0
    start_vertex = next((vertex for vertex, deg_diff in out_degree.items() if deg_diff > 0), None)

    if start_vertex is None:
        return None

    dfs(0)
    eulerian_path.insert(0, start_vertex)

    # Check if all edges are visited
    all_edges_visited = all(len(neighbors) == 0 for neighbors in graph.values())

    if all_edges_visited:
        return eulerian_path
    else:
        return None

# Example usage:
# Represent the graph as an adjacency list
graph = {
    0: [2],
    1: [3],
    2: [1],
    3: [0, 4],
    6: [3, 7],
    7: [8],
    8: [9],
    9: [6]
}

eulerian_path = find_eulerian_path(graph)

if eulerian_path:
    print("Eulerian Path:", '->'.join(map(str, eulerian_path)))
else:
    print("No Eulerian Path exists.")
