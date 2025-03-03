def findMin(nums):
    res = nums[0]
    left = 0
    right = len(nums) - 1

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        mid = (left + right) // 2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return res

arr = [4,5,6,7,0,1,2]
print(findMin(arr))