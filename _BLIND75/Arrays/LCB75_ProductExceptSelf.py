def productExceptSelf(nums):
    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    for j in range(len(nums) - 2, -1, -1):
        right[j] = right[j + 1] * nums[j + 1]

    for k in range(len(nums)):
        nums[k] = left[k] * right[k]

    return nums

arr = [1,2,3,4]
print(productExceptSelf(arr))