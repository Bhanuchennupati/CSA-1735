from collections import deque

def is_valid(state):
    x, y = state
    return 0 <= x <= 4 and 0 <= y <= 3

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        (current, path) = queue.popleft()
        (x, y) = current

        if current == goal:
            return path + [current]

        # List of all possible actions
        actions = [
            (4, y),    # Fill Jug A
            (x, 3),    # Fill Jug B
            (0, y),    # Empty Jug A
            (x, 0),    # Empty Jug B
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # Pour A to B
            (x + min(y, 4 - x), y - min(y, 4 - x)),  # Pour B to A
        ]

        for action in actions:
            if is_valid(action) and action not in visited:
                visited.add(action)
                queue.append((action, path + [current]))

    return None

def solve_water_jug():
    start = (0, 0)  # Initial state: Both jugs are empty
    goal = (2, 0)   # Goal state: 4-gallon jug has exactly 2 gallons of water

    solution = bfs(start, goal)
    if solution:
        print("Solution found:")
        for state in solution:
            print(state)
    else:
        print("No solution exists.")

# Example usage:
solve_water_jug()
