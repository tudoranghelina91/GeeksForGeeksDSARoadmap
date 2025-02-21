def separateNegativePositive(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr

print(separateNegativePositive([11, 5, 2, -1, 3, -2, -14, 5, 10, -6]))