from collections import deque

# Function to solve the 8-puzzle problem using BFS
def solve_8_puzzle(start, goal):
    queue = deque([(start, [])])  # (current state, path to reach it)
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:  # Goal state reached
            return path + [state]

        visited.add(tuple(state))
        zero = state.index(0)  # Find the empty space (0)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        row, col = divmod(zero, 3)

        for dr, dc in moves:
            r, c = row + dr, col + dc
            if 0 <= r < 3 and 0 <= c < 3:  # Check boundaries
                new_zero = r * 3 + c
                new_state = state[:]
                new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
                if tuple(new_state) not in visited:
                    queue.append((new_state, path + [state]))
    return None

# Initial and goal states
start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Solve the puzzle
solution = solve_8_puzzle(start, goal)

# Print all steps
if solution:
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution found.")
