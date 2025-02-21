def traverse(M, i, j):
    if i == len(M) and j == len(M[0]):
        return
    
    print(M[i][j], end=" ")

    if j < len(M[0]) - 1:
        traverse(M, i, j + 1)
        return
    
    if i < len(M) - 1:
        traverse(M, i + 1, 0)
        return

M = [[1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]]

traverse(M, 0, 0)