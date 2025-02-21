def subtractMatrices(A, B):
    n = len(A)
    m = len(A[0])

    C = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] - B[i][j]

    return C

A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 1, 1], [1, 1, 1]]

C = subtractMatrices(A, B)
print(C)