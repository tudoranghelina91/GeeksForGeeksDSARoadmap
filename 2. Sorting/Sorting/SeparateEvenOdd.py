def separateEvenOdd(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr

print(separateEvenOdd([1, 5, 22, 30, 14, 9, 2]))