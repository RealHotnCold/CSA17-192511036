from collections import deque

capacity_a = 4
capacity_b = 3
goal = 2

def get_next_states(state):
    a, b = state
    states = [
        ((capacity_a, b), "Fill Jug A"),
        ((a, capacity_b), "Fill Jug B"),
        ((0, b), "Empty Jug A"),
        ((a, 0), "Empty Jug B")
    ]

    amount = min(a, capacity_b - b)
    states.append(((a - amount, b + amount), "Pour A -> B"))

    amount = min(b, capacity_a - a)
    states.append(((a + amount, b - amount), "Pour B -> A"))

    return states

def solve():
    queue = deque([((0, 0), [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state[0] == goal or state[1] == goal:
            return path + [("Goal", state)]

        for next_state, action in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [(action, next_state)]))

    return None

solution = solve()

if solution:
    print("Solution:")
    print("(0, 0)")
    for action, state in solution:
        print(action, "->", state)
else:
    print("No solution.")
