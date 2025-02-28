def sumOfMiddleRowsCols(mat):
    n = len(mat)

    mid = int((n - 1) / 2)

    rowsum = 0
    colsum = 0

    for j in range(n):
        rowsum += mat[mid][j]

    for i in range(n):
        colsum += mat[i][mid]

    return [rowsum, colsum]

print(sumOfMiddleRowsCols([
    [2, 5, 7],
    [3, 7, 2], 
    [5, 6, 9]])
)