# Program 10: A* Search Algorithm
import heapq
graph = {"A":{"B":1,"C":4}, "B":{"C":2,"D":5},
         "C":{"D":1}, "D":{}}
heuristic = {"A":4, "B":3, "C":1, "D":0}
def astar(start, goal):
    heap = [(heuristic[start], 0, start, [start])]
    best = {start: 0}
    while heap:
        f, g, node, path = heapq.heappop(heap)
        if node == goal:
            return path, g
        if g != best.get(node):
            continue
        for nxt, weight in graph[node].items():
            new_g = g + weight
            if new_g < best.get(nxt, float("inf")):
                best[nxt] = new_g
                heapq.heappush(heap, (new_g + heuristic[nxt], new_g,
                                      nxt, path + [nxt]))
    return None, float("inf")
start = input("Start node (A-D): ").strip().upper()
goal = input("Goal node (A-D): ").strip().upper()
if start in graph and goal in graph:
    path, total = astar(start, goal)
    print("Path:", " -> ".join(path) if path else "No path found")
    if path:
        print("Total cost:", total)
else:
    print("Invalid node.")
