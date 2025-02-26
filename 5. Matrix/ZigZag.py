def zig_zag_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    row = 0
    col = 0

    # Boolean variable that is true if we need
    # to increment 'row' value;
    # otherwise, false if we increment 'col' value.
    row_inc = False

    # Print the first half of the zig-zag pattern
    mn = min(m, n)
    for length in range(1, mn + 1):
        for i in range(length):
            print(mat[row][col], end=' ')

            if i + 1 == length:
                break

            # If row_inc is true, increment row 
            # and decrement col;
            # otherwise, decrement row and increment col.
            if row_inc:
                row += 1
                col -= 1
            else:
                row -= 1
                col += 1

        if length == mn:
            break

        # Update row or col value based on the
        # last increment
        if row_inc:
            row += 1
            row_inc = False
        else:
            col += 1
            row_inc = True

    # Adjust row and col for the second half of the matrix
    if row == 0:
        if col == m - 1:
            row += 1
        else:
            col += 1
        row_inc = True
    else:
        if row == n - 1:
            col += 1
        else:
            row += 1
        row_inc = False

    # Print the second half of the zig-zag pattern
    MAX = max(m, n) - 1
    for diag in range(MAX, 0, -1):
        length = mn if diag > mn else diag
        for i in range(length):
            print(mat[row][col], end=' ')

            if i + 1 == length:
                break

            # Update row or col value based on the last increment
            if row_inc:
                row += 1
                col -= 1
            else:
                col += 1
                row -= 1

        # Update row and col based on position in the matrix
        if row == 0 or col == m - 1:
            if col == m - 1:
                row += 1
            else:
                col += 1
            row_inc = True
        elif col == 0 or row == n - 1:
            if row == n - 1:
                col += 1
            else:
                row += 1
            row_inc = False

# Driver code
if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    zig_zag_matrix(mat)