
# Assessment 3.3
# Non-linear Data Structure
# Student: JABERINA
# Program: Graph

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B'],
    'F': ['C'],
    'G': ['D']
}


# Display Graph
def display_graph():
    print("\nGRAPH CONNECTIONS")
    for vertex, edges in graph.items():
        print(vertex, ":", edges)


# Breadth First Search
def bfs(start):
    visited = []
    queue = [start]

    while queue:
        current = queue.pop(0)

        if current not in visited:
            visited.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited


# Depth First Search
def dfs(vertex, visited=None):
    if visited is None:
        visited = []

    visited.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited)

    return visited


print("================================")
print("      JABERINA - GRAPH")
print("================================")

display_graph()

print("\nBreadth First Search (BFS):")
print(bfs('A'))

print("\nDepth First Search (DFS):")
print(dfs('A'))

print("\n================================")
