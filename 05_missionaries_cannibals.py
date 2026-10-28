from collections import deque

start = (3, 3, "L")
goal = (0, 0, "R")

moves = [
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (1, 1)
]

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True

def get_next_states(state):
    m, c, boat = state
    next_states = []

    for dm, dc in moves:
        if boat == "L":
            new_state = (m - dm, c - dc, "R")
        else:
            new_state = (m + dm, c + dc, "L")

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def solve():
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

solution = solve()

if solution:
    print("Solution:\n")
    for state in solution:
        print(state)
else:
    print("No solution found.")
