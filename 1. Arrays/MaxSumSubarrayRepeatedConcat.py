def max_sum_subarr_repeated(arr, k):
    n = len(arr)
    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(n * k):
        # Use modular arithmetic to get the next element
        max_ending_here += arr[i % n]
        max_so_far = max(max_so_far, max_ending_here)

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

print(max_sum_subarr_repeated([10, 20, -30, -1], 3))