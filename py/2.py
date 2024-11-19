def dfs(graph, start):
    visited = set()  # To track visited nodes
    stack = [start]  # Initialize the stack with the starting node

    while stack:
        node = stack.pop()  # LIFO: Get the last added node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark the node as visited
            stack.extend(graph[node])  # Add neighbors to the stack

# Graph representation from the image
graph = {
    0: [1, 2],
    1: [1],
    2: [0, 3],
    3: [3]
}

# Perform DFS starting from node 2
dfs(graph, 2)
