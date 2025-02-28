def shiftRowWiseByK(mat, k):
    for i in range(len(mat)):
        out = []

        # Module trick works too
        # for j in range(len(mat[0])):
        #     out.append(mat[i][(j + k) % len(mat[0])])

        for j in range(k, len(mat[0])):
            out.append(mat[i][j])
        
        for j in range(k):
            out.append(mat[i][j])

        mat[i] = out

mat = [[1, 2, 3, 4], 
       [5, 6, 7, 8], 
       [9, 10, 11, 12], 
       [13, 14, 15, 16]] 
k = 2

shiftRowWiseByK(mat, k)
print(mat)