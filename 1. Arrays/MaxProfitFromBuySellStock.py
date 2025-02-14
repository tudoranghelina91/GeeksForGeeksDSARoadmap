def maximumProfit(prices) -> int:
    sum = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            sum += prices[i] - prices[i - 1]
    
    return sum

arr = [100, 180, 260, 310, 40, 535, 695]
print(maximumProfit(arr))