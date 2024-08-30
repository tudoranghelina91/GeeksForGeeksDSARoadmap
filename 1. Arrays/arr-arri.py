# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(arr)

i = 0

# loop through and keep swapping as long as arr[i] not equal to i
while (i < len(arr)):
    if arr[i] != i and arr[i] >= 0:
        aux = arr[arr[i]]
        arr[arr[i]] = arr[i]
        arr[i] = aux
        continue
    i = i + 1

print(arr)