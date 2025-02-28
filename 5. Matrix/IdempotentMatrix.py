# Idempotent matrix means that if it is multiplied by itself, it will return the same matrix
def multiply(A, B):
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

def isIdempotent(mat):
    B = multiply(mat, mat)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (B[i][j] != mat[i][j]):
                return False
            
    return True

# TODO FIX THIS
print(isIdempotent([
    [2, -2, -4],
    [-1, 3, 4],
    [1, -2, 3]
]))

