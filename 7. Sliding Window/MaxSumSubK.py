# Main idea is to initialize the first subarray sum
# iterate over array in forward-only manner, by always subtracting
"""
Main idea is to initialize the first subarray sum
iterate over array in forward-only manner, by always subtracting
the starting element and adding the last element after the current "window"
"""

def maxSumSubArr(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(maxSumSubArr([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))