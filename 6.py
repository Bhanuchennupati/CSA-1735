from collections import deque

def is_goal(state):
    _, grid = state
    return all(cell == 0 for row in grid for cell in row)

def get_successors(state):
    (x, y), grid = state
    successors = []
    rows, cols = len(grid), len(grid[0])

    # Move up
    if x > 0:
        successors.append(((x - 1, y), grid))
    # Move down
    if x < rows - 1:
        successors.append(((x + 1, y), grid))
    # Move left
    if y > 0:
        successors.append(((x, y - 1), grid))
    # Move right
    if y < cols - 1:
        successors.append(((x, y + 1), grid))
    # Clean the current room
    if grid[x][y] == 1:
        new_grid = [row[:] for row in grid]
        new_grid[x][y] = 0
        successors.append(((x, y), new_grid))

    return successors

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(map(tuple, start[1])))

    while queue:
        (current_state, path) = queue.popleft()
        if is_goal(current_state):
            return path + [current_state]
        
        for next_state in get_successors(current_state):
            state_tuple = (next_state[0], tuple(map(tuple, next_state[1])))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((next_state, path + [current_state]))
    return None

def solve_vacuum_cleaner(initial_position, grid):
    start = (initial_position, grid)
    solution = bfs(start)
    if solution:
        print("Solution found:")
        for state in solution:
            print(state)
    else:
        print("No solution exists.")

# Example usage:
initial_position = (0, 0)
grid = [
    [1, 0, 1],
    [1, 1, 0],
    [0, 0, 1]
]

solve_vacuum_cleaner(initial_position, grid)
