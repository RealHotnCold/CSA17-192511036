from heapq import heappush, heappop

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        goal_pos = state[i] - 1
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_pos, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_pos = nr * 3 + nc
            new_state = list(state)
            new_state[blank], new_state[new_pos] = new_state[new_pos], new_state[blank]
            neighbors.append(tuple(new_state))
    return neighbors

def solve(start):
    pq = []
    heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heappop(pq)
        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            return path

        for next_state in get_neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                heappush(pq, (new_g + heuristic(next_state), new_g,
                              next_state, path))
    return None

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()

start = tuple(map(int, input("Enter 9 values (0 for blank): ").split()))
solution = solve(start)

if solution:
    print("\nSolution:")
    for state in solution:
        display(state)
    print("Number of moves:", len(solution) - 1)
    input()
else:
    print("No solution found.")
    input()
