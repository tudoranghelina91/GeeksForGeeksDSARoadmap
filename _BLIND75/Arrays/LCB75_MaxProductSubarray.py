def maxProduct(nums):
    res = max(nums)
    curMin, curMax = 1, 1

    for num in nums:
        # Edge case for current number zero - didn't happen on LC
        # For efficiency
        # if num == 0:
        #     curMin, curMax = 1, 1
        #     continue

        tmpmax = curMax * num
        tmpmin = curMin * num

        curMax = max(tmpmax, tmpmin, num)
        curMin = min(tmpmax, tmpmin, num)
        res = max(res, curMax)

    return res