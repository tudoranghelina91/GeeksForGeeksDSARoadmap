def boundaryTraversal(mat):
    n = len(mat)
    m = len(mat[0])
    out = []
    
    for j in range(m):
        out.append(mat[0][j])
    
    for i in range(1, n):
        out.append(mat[i][m - 1])
        
    for j in range(m - 2, -1, -1):
        out.append(mat[n - 1][j])
        
    for i in range(n - 2, 0, -1):
        out.append(mat[i][0])
        
    return out

print(boundaryTraversal([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15,16]]))