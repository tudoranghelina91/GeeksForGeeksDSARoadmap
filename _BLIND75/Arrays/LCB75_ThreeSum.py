def threeSum(nums):
    output = []
    nums.sort()

    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while l < r:
            threesum = nums[i] + nums[l] + nums[r]

            if threesum < 0:
                l += 1
            
            elif threesum > 0:
                r -= 1

            else:
                output.append([nums[i], nums[l], nums[r]])
                while(True):
                    l += 1
                    if l >= r or nums[l] != nums[l - 1]:
                        break
    return output

# Example usage
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]