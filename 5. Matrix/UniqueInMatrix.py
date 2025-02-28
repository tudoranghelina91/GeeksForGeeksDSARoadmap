def uniqueInMatrix(mat):
    occurences = {}

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] not in occurences:
                occurences[mat[i][j]] = 0

            occurences[mat[i][j]] += 1

    out = []
    for key in occurences:
        if occurences[key] == 1:
            out.append(key)

    return out

print(uniqueInMatrix([
    [2, 1, 4, 3],
    [1, 2, 3, 2],
    [3, 6, 2, 3],
    [5, 2, 5, 3]]
))