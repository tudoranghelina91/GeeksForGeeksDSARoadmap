def maxPerRow(mat):
    out = []

    for i in range(len(mat)):
        maximum = mat[i][0]
        for j in range(1, len(mat[0])):
            maximum = max(maximum, mat[i][j])
        out.append(maximum)

    return out

print(maxPerRow([[1, 2, 3], [1, 4, 9], [76, 34, 21]]))