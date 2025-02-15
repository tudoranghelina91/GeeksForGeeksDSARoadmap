def kadane(arr):
    max1 = max2 = arr[0]
    
    for num in arr[1:]:
        max1 = max(num, max1 + num)
        max2 = max(max1, max2)
    
    return max2

print(kadane([1, 2, 3, -2, 5]))