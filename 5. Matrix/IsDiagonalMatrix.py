# Diagonal matrix is a matrix that has all the elements equal to zero except the ones on the main diagonal

def isDiagonal(mat):
    n = len(mat)

    for i in range(n):
        for j in range(n):
            if i != j and mat[i][j] != 0:
                return False
            
    return True

mat = [[4, 0, 0, 0],
        [0, 5, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 1]]

print(isDiagonal(mat))