def segregate0and1(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] == 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

arr = [0,1,1,0,0,1,0,1]
print(arr)
segregate0and1(arr)
print(arr)