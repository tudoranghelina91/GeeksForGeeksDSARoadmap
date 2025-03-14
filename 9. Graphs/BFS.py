"""
The idea is to pass an adjacency list as an argument
We instantiate the visited array with false values and populate it as we visit the graph
We loop through the nodes so we can include disconnected edges too
"""
def bfs(adj):
    visited = [False] * len(adj)
    output = []

    for node in range(len(adj)):
        if not visited[node]:
            visited[node] = True
            queue = [node]

            output2 = []
            while queue:
                parent = queue.pop(0)
                output2.append(parent)
                
                for child in adj[parent]:
                    if not visited[child]:
                        visited[child] = True
                        queue.append(child)

            output.append(output2)

    return output               
                

# Example 1
adj = [
    [1, 2],
    [0], 
    [0], 
    [4], 
    [3, 5], 
    [4]
]
print(bfs(adj))

# Example 2
adj = [
    [1, 3], 
    [0, 2], 
    [1, 3], 
    [0, 2]
]
print(bfs(adj))

# Example 3
adj = [
    [1], 
    [0, 2, 3], 
    [1], 
    [1]
]
print(bfs(adj))

# Example 4
adj = [
    [1, 2, 3], 
    [0], 
    [0], 
    [0, 4], 
    [3]
]
print(bfs(adj))

# Example 5
adj = [
    [1, 4], 
    [0, 2, 3], 
    [1], 
    [1], 
    [0]
]
print(bfs(adj))