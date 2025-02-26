# Function to get cofactor of mat[p][q] in cof[][]
def get_cof(mat, cof, p, q, n):
    i = 0
    j = 0
    for row in range(n):
        for col in range(n):
            if row != p and col != q:
                cof[i][j] = mat[row][col]
                j += 1
                if j == n - 1:
                    j = 0
                    i += 1

# Recursive function for finding determinant
# of matrix mat of dimension n
def get_det(mat, n):
    if n == 1:
        return mat[0][0]
    det = 0
    cof = [[0] * n for _ in range(n)]  # To store cofactors
    sign = 1
    for f in range(n):
        get_cof(mat, cof, 0, f, n)
        det += sign * mat[0][f] * get_det(cof, n - 1)
        sign = -sign
    return det

# Function to get adjoint of mat in adj
def adjoint(mat, adj):
    n = len(mat)
    if n == 1:
        adj[0][0] = 1
        return
    sign = 1
    cof = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            get_cof(mat, cof, i, j, n)
            sign = 1 if (i + j) % 2 == 0 else -1
            adj[j][i] = sign * get_det(cof, n - 1)

# Function to calculate and store inverse, returns 
# false if matrix is singular
def inverse(mat):
    n = len(mat)
    det = get_det(mat, n)
    if det == 0:
        print("Singular matrix, can't find its inverse")
        return None
    adj = [[0] * n for _ in range(n)]
    adjoint(mat, adj)
    inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]
    return inv

if __name__ == '__main__':
    mat = [[5, -2, 2, 7], [1, 0, 0, 3], [-3, 1, 5, 0], [3, -1, -9, 4]]
    n = len(mat)
    adj = [[0] * n for _ in range(n)]  # To store adjoint

    # Print the input matrix
    print("Input matrix is:")
    for row in mat:
        print(row)

    # Print the adjoint matrix
    print("\nThe Adjoint is:")
    adjoint(mat, adj)
    for row in adj:
        print(row)

    # Print the inverse matrix if it exists
    print("\nThe Inverse is:")
    inv = inverse(mat)
    if inv:
        for row in inv:
            print(row)
