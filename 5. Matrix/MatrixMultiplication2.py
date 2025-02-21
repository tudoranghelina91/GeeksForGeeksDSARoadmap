def multiply(A, B, C, n):
    # Code here
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

A = [[7, 8], [2, 9]]
B = [[14, 5], [5, 18]]
n = len(A)

C = [[0] * n for _ in range(n)]

print(multiply(A, B, C, n))

