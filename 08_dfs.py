# Program 8: Depth First Search
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
         "D": [], "E": ["F"], "F": []}
def dfs(node, visited):
    if node in visited:
        return
    print(node, end=" ")
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)
start = input("Start node (A-F): ").strip().upper()
if start in graph:
    print("DFS traversal:")
    dfs(start, set())
    print()
else:
    print("Invalid node.")
