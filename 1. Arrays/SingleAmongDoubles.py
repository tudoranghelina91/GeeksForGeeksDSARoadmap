# XOR ^ operator

def singleAmongDoubles(arr):
    n = len(arr)

    res = 0

    for num in arr:
        res = res ^ num

    return res

print(singleAmongDoubles([2, 3, 5, 4, 5, 3, 4]))