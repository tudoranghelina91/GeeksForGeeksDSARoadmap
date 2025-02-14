def missingNumber(arr):
    # code here
    map = []
    for i in range (len(arr) + 2):
        map.append(False)
    
    for num in arr:
        map[num] = True
        
    for i in range(1, len(map)):
        if not map[i]:
            return i

print(missingNumber([3, 2, 5, 4]))