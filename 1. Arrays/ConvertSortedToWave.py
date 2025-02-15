def convertToWave(arr):
    for i in range(1, len(arr), 2):
        arr[i - 1], arr[i] = arr[i], arr[i - 1]

arr = [1, 2, 3, 4, 5]
convertToWave(arr)
print(arr)