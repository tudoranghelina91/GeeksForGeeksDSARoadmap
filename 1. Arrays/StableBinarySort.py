# Two partition algorithms for the same problem

def stableBinarySortNaive(arr):
    even = [x for x in arr if x % 2 == 0]   
    odd = [x for x in arr if x % 2 != 0]
    return even + odd

def stableBinarySortLomuto(arr):
    i = -1
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr

print(stableBinarySortNaive([-5, -2, 0, 4, 7, 9]))
print(stableBinarySortLomuto([-5, -2, 0, 4, 7, 9]))
