def isScalar(mat):
    n = len(mat)
    firstItem = mat[0][0]

    for i in range(n):
        for j in range(n):
            if (i != j and mat[i][j] != 0) or (i == j and mat[i][j] != firstItem):
                return False
            
    return True

mat = [[ 4, 0, 0, 0 ],
       [ 0, 4, 0, 0 ],
       [ 0, 0, 4, 0 ],
       [ 0, 0, 0, 4 ]]

print(isScalar(mat))