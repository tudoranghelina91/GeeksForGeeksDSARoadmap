# Can go left 1 step max
# Can go down 1 step max
# Can go diagonally left until a margin is encountered
# Can go diagonally right until a margin is encountered

# L = 1, R = 0, D = 0, U = 0

# 1. Go left 1 step
# 2. Set go left false
# 3. Set go down true
# 4. Set go right true

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

i = 0
j = 0

n = len(mat)
m = len(mat[0])

right = 1 # right vector
down = 0 # down vector

while i < n and j < m:
    print(mat[i][j], end = " ")
    j = j + right
    right = -1 # change direction of vector
    down = 1

    while j >= 0 or j < len(mat[0]):
        print(mat[i][j], end = " ")
        i = i + down
        j = j + right
    
    # Go down one step
    i = i + down
    down = -1
    right = 0

# down and left we can go only one step per iteration
# diagonally up and down we can go until we reach the margin