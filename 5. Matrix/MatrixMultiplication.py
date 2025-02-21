def multiplyMatrices(A, B):
    n1 = len(A)
    m1 = len(A[0])

    n2 = len(B)
    m2 = len(B[0])
    
    C = [[0] * m2 for _ in range(n1)]

    for i in range(n1):
        for j in range(n2):
            for k in range(m1):
                C[i][j] += A[i][k] * B[k][j]

    return C

A = [
    [1, 1],
    [2, 2]
]

B = [
    [1, 1],
    [2, 2]
]

C = multiplyMatrices(A, B)

print(C)