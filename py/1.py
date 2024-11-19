from collections import deque

def bfs(graph, start):
    visited = set()  # To track visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue the first node
        if node not in visited:
            print(node, end=" ")  # Process the node (e.g., print it)
            visited.add(node)  # Mark the node as visited
            queue.extend(graph[node])  # Enqueue all unvisited neighbors

# Graph representation based on the image
graph = {
    0: [1, 2],
    1: [1],
    2: [0, 3],
    3: [3]
}

# Perform BFS starting from node 2 (start)
bfs(graph, 2)
