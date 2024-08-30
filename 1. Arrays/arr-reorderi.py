# Input:  arr[]   = [10, 11, 12];
#             index[] = [1, 0, 2];
# Output: arr[]   = [11, 10, 12]
#            index[] = [0,  1,  2] 

# Input:  arr[]   = [50, 40, 70, 60, 90]
#           index[] = [3,  0,  4,  1,  2]
# Output: arr[]   = [40, 60, 90, 50, 70]
#           index[] = [0,  1,  2,  3,   4]

arr = [50, 40, 70, 60, 90]
index = [3,  0,  4,  1,  2]

ordered = [0, 0, 0, 0, 0]
k = 0

for i in index:
    ordered[i] = arr[k]
    k = k + 1

print(ordered)