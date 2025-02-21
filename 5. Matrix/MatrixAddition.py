def addMatrices(A, B):
    n = len(A)
    m = len(A[0])

    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]

    return C

A = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]
B = [ [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4] ]
print(addMatrices(A,B))