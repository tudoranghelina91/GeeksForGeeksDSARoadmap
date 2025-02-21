def searchInMatrix(mat, target):
    n = len(mat)
    m = len(mat[0])

    for i in range(0, n):
        for j in range(0, m):
            if target == mat[i][j]:
                return True
            
    return False


mat = [
    [10, 51, 9],
    [14, 20, 21],
    [30, 24, 43]
]
print(searchInMatrix(mat, 14))