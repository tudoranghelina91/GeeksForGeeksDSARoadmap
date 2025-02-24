def maximumProfit(prices) -> int:
    minimum = prices[0]
    profit = 0

    for i in range(len(prices)):
        profit = max(profit, prices[i] - minimum)
        minimum = min(minimum, prices[i])

    return profit

arr = [100, 180, 260, 310, 40, 535, 695]
print(maximumProfit(arr))