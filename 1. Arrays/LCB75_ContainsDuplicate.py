def containsDuplicate(nums):
    occurences = {}
    for num in nums:
        if num in occurences:
            return True
        
        occurences[num] = True
    
    return False

print(containsDuplicate([1, 5, 9, 2, 8, 2]))