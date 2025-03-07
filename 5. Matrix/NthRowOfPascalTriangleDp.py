def nthRowOfPascalTriangle(n):
    # code here
    mat = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == j or j == 0:
                row.append(1)
            else:
                row.append(mat[i - 1][j - 1] + mat[i - 1][j])
                
        mat.append(row)
    
    return mat[n - 1]

print(nthRowOfPascalTriangle(10000)) # [1, 5, 10, 10, 5, 1]