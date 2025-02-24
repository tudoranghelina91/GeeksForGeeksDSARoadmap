def subarraySum(self, arr, target):
    # code here
    i = j = 0
    sum = 0
    while j < len(arr):
        sum += arr[j]
            
        while (sum > target):
            sum -= arr[i]
            i += 1
            
        if sum == target:
            return [i + 1, j + 1]
        
        j += 1

    return [-1]