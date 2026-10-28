# Program 7: Breadth First Search
from collections import deque
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
         "D": [], "E": ["F"], "F": []}
def bfs(start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(n for n in graph[node] if n not in visited)
start = input("Start node (A-F): ").strip().upper()
if start in graph:
    print("BFS traversal:")
    bfs(start)
    print()
else:
    print("Invalid node.")
