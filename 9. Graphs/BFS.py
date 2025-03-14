"""
The idea is to pass an adjacency list as an argument
We instantiate the visited array with false values and populate it as we visit the graph
We loop through the nodes so we can include disconnected edges too
"""

def bfs(adj):
    nodes = len(adj)
    visited = [False] * nodes

    for node in range(nodes):
        if not visited[node]:
            queue = []
            visited[node] = True
            queue.append(node)

            while queue:
                parent = queue.pop(0)
                
                print(parent, end = " ")

                for child in adj[parent]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append(child)

            print("|", end = " ")

    print()


# Example 1
adj = [
    [1, 2],
    [0], 
    [0], 
    [4], 
    [3, 5], 
    [4]
]
bfs(adj)

# Example 2
adj = [
    [1, 3], 
    [0, 2], 
    [1, 3], 
    [0, 2]
]
bfs(adj)

# Example 3
adj = [
    [1], 
    [0, 2, 3], 
    [1], 
    [1]
]
bfs(adj)

# Example 4
adj = [
    [1, 2, 3], 
    [0], 
    [0], 
    [0, 4], 
    [3]
]
bfs(adj)

# Example 5
adj = [
    [1, 4], 
    [0, 2, 3], 
    [1], 
    [1], 
    [0]
]
bfs(adj)