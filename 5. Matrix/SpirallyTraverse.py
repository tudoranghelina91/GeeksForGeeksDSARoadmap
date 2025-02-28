def spirallyTraverse(mat):
    # code here
    n = len(mat)
    m = len(mat[0])
    
    istart = 0
    iend = n - 1
    
    jstart = 0
    jend = m - 1
    
    out = []
    
    while istart <= iend and jstart <= jend:
        for j in range(jstart, jend + 1):
            out.append(mat[istart][j])
        istart += 1
        
        for i in range(istart, iend + 1):
            out.append(mat[i][jend])
        jend -= 1
        
        if istart <= iend:
            for j in range(jend, jstart - 1, -1):
                out.append(mat[iend][j])
            iend -= 1

        if jstart <= jend:
            for i in range(iend, istart - 1, -1):
                out.append(mat[i][jstart])
            jstart += 1
        
    return out

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(spirallyTraverse(mat))