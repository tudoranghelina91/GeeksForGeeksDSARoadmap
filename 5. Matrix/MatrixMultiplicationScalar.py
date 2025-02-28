def multiplyScalar(mat, x):
    n = len(mat)
    m = len(mat[0])

    res = [[0] * m for _ in range(n)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            res[i][j] = mat[i][j] * x

    return res

mat = [[1,2,3],[4,5,6],[7,8,9]]

print(multiplyScalar(mat, 2))