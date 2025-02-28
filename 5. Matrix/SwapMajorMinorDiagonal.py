def swapDiagonals(mat):
    n = len(mat)
    for i in range(n):
        mat[i][i], mat[i][n - 1 - i] = mat[i][n - 1 - i], mat[i][i]



mat = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
swapDiagonals(mat)
print(mat)