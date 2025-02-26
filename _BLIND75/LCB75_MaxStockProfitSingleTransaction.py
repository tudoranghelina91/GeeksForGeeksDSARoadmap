def maximumProfit(prices):
    # code here
    minimum = prices[0]
    profit = 0

    for i in range(len(prices)):
        profit = max(profit, prices[i] - minimum)
        minimum = min(minimum, prices[i])

    return profit

arr = [7, 10, 1, 3, 6, 9, 2]
print(maximumProfit(arr))