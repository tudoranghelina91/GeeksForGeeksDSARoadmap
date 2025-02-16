def largest(arr):
    maxnum = 0
    for num in arr:
        maxnum = max(maxnum, num)
        
    return maxnum

print(largest([3, 1, 2, 72, 12, 5]))