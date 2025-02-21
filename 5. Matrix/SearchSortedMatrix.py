def searchInSortedMatrix(M, key):
    n = len(M)
    m = len(M[0])

    lo, hi = 0, n * m - 1
    while lo <= hi:
        mid = (lo + hi) // 2

        row = mid // m
        col = mid % m

        if M[row][col] == key:
            return True

        if M[row][col] < key:
            lo = mid + 1

        else:
            hi = mid - 1

print(searchInSortedMatrix([
    [1, 5, 9],
    [14, 20, 21],
    [30, 34, 43]
], 14))