def maxSubArray(nums):
    max1 = -10000
    max2 = -10000

    for num in nums:
        max1 = max(num, num + max1)
        max2 = max(max1, max2)
    
    return max2