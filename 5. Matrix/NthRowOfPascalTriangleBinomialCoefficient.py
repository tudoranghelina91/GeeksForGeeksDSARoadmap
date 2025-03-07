def nthRowOfPascalTriangle(n):
    # code here
    mat = []
    for i in range(1, n + 1):
        # combinari de n luate cate k
        c = 1
        row = []
        for j in range(1, i + 1):
            # first row always 1
            row.append(c)
            c = c * (i - j) // j
        mat.append(row)

    return mat[-1]

print(nthRowOfPascalTriangle(5)) # [1, 4, 6, 4, 1]