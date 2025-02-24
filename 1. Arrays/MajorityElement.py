def majorityElement(arr):
    map = {}
    
    for num in arr:
        if num not in map:
            map[num] = 0
        
        map[num] += 1
        
    for key in map:
        if map[key] > len(arr) / 2:
            return key

    return -1

arr = [3, 1, 3, 3, 2]

print(majorityElement(arr))