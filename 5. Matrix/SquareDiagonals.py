def squareDiagonals(mat):
    n = len(mat)
    primary = []
    secondary = []

    for i in range(n):
        primary.append(mat[i][i] * mat[i][i])
        secondary.append(mat[i][n - 1 - i] * mat[i][n - 1 - i])

    return [primary, secondary]

mat = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(squareDiagonals(mat))