def spiralOrder(matrix):
    left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)

    out = []
    while top < bottom and left < right:
        for j in range(left, right):
            out.append(matrix[top][j])
        top += 1

        for i in range(top, bottom):
            out.append(matrix[i][right - 1])
        right -= 1

        if top < bottom:
            for j in range(right - 1, left - 1, -1):
                out.append(matrix[bottom - 1][j])
            bottom -= 1

        if left < right:
            for i in range(bottom - 1, top - 1, -1):
                out.append(matrix[i][left])
            left += 1

    return out

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralOrder(matrix)) # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]