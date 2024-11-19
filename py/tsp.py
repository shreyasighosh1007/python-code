from itertools import permutations

graph = [
    [0, 10, 15, 20],  # Node 1
    [10, 0, 35, 25],  # Node 2
    [15, 35, 0, 30],  # Node 3
    [20, 25, 30, 0],  # Node 4
]

# Number of nodes
n = len(graph)

# Generate all possible routes starting at node 1 (0 in 0-based indexing)
routes = permutations(range(1, n))  # Fix node 0 as the start point

min_distance = float('inf')
best_route = []

# Calculate distances for all routes
for route in routes:
    # Include the starting node (0) at the beginning and end
    current_route = [0] + list(route) + [0]
    distance = sum(graph[current_route[i]][current_route[i + 1]] for i in range(len(current_route) - 1))
    
    if distance < min_distance:
        min_distance = distance
        best_route = current_route

# Convert route to 1-based indexing
best_route = [node + 1 for node in best_route]

# Print results
print(f"Minimum distance: {min_distance}")
print(f"Optimal route: {best_route}")
