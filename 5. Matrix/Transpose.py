def transpose(M):
    n = len(M)
    m = len(M[0])
    for i in range(n):
        for j in range(i, m):
            M[i][j], M[j][i] = M[j][i], M[i][j]

    return M

print(transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))