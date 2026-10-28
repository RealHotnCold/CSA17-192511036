# Program 9: Travelling Salesman Problem using brute force
from itertools import permutations
cities = ["A", "B", "C", "D"]
dist = {("A","B"):10, ("A","C"):15, ("A","D"):20,
        ("B","C"):35, ("B","D"):25, ("C","D"):30}
def cost(a, b):
    return dist.get((a,b), dist.get((b,a), 0))
best_route, best_cost = None, float("inf")
for order in permutations(["B", "C", "D"]):
    route = ("A",) + order + ("A",)
    total = sum(cost(route[i], route[i+1]) for i in range(len(route)-1))
    if total < best_cost:
        best_route, best_cost = route, total
print("Best route:", " -> ".join(best_route))
print("Minimum distance:", best_cost)
