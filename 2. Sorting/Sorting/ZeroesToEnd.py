def zeroesToEnd(arr): # lomuto
    i = -1
    for j in range(len(arr)):
        if arr[j] == 1:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr

print(zeroesToEnd([1,1,0,1,0,1,0,0,1,1]))