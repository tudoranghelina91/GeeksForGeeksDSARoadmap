# Lomuto partition O(n)

def rearrange(n, arr):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

arr = [3, 2, -1, 5, -10, -12]
rearrange(len(arr), arr)
print(arr)