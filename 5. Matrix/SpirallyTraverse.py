def spirallyTraverse(mat):
    # code here
    n = len(mat)
    m = len(mat[0])
    
    istart = 0
    iend = n
    
    jstart = 0
    jend = m
    
    out = []
    
    while istart < iend and jstart < jend:
        for j in range(jstart, jend):
            out.append(mat[istart][j])
        istart += 1
        
        for i in range(istart, iend):
            out.append(mat[i][jend - 1])
        jend -= 1
        
        if istart < iend:
            for j in range(jend - 1, jstart - 1, -1):
                out.append(mat[iend - 1][j])
            iend -= 1

        if jstart < jend:
            for i in range(iend - 1, istart - 1, -1):
                out.append(mat[i][jstart])
            jstart += 1
        
    return out

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(spirallyTraverse(mat))