def determinantOfMatrix(matrix,n):
    # code here
    if n == 1:
        return matrix[0][0]
        
    if n == 2:
        return matrix[0][0] * matrix[1][1] - \
                matrix[0][1] * matrix[1][0]
                
    res = 0
    for col in range(n):
        # create submatrix
        sub = [[0] * (n - 1) for _ in range(n - 1)]
        
        # set submatrix
        for i in range(1, n):
            subcol = 0
            for j in range(n):
                if j == col:
                    continue
                
                sub[i - 1][subcol] = matrix[i][j]
                subcol += 1
                
        # Cofactor expansion
        sign = 1 if col % 2 == 0 else -1
        res += sign * matrix[0][col] * determinantOfMatrix(sub, n - 1)
    
    return res

matrix = [
            [1, 0, 2, -1],
            [3, 0, 0, 5],
            [2, 1, 4, -3],
            [1, 0, 5, 0]
        ]

print(determinantOfMatrix(matrix, len(matrix)))