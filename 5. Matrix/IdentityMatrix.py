def isIdentityMatrix(mat):
    n = len(mat)
    m = len(mat[0])

    for i in range(n):
        for j in range(m):
            if (i != j and mat[i][j] != 0) or (i == j and mat[i][j] != 1):
                return False
            
    return True


identity = [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]

notidentity = [[6, 10, 12, 0],
                [0, 5, 0, 0],
                [0, 0, 9, 0],
                [0, 0, 0, 1]]

print(isIdentityMatrix(identity))
print(isIdentityMatrix(notidentity))