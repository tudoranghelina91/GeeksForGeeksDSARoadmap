def twoSum(arr, target):
    # Your code here
    map = {}
    
    for num in arr:
        if num in map:
            return [map[num], num]
        
        map[target - num] = num
        
    return []

arr = [2, 9, 10, 4, 15]
target = 12

print(twoSum(arr, target))