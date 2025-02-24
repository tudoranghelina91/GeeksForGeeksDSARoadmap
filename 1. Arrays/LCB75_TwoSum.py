def twoSum(nums, target):
    map = {}
    
    i = 0
    for i in range(len(nums)):
        if target - nums[i] in map:
            return [i, map[target - nums[i]]]

        else:
            map[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))