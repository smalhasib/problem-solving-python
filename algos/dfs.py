def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start)
        visited.add(start)
        for neighbor in graph.get(start, []):
            dfs(graph, neighbor, visited)

# Example usage:
# Create an adjacency list representation of the graph
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

# Perform DFS starting from node 1
print("DFS starting from node 1:")
dfs(graph, 1)
