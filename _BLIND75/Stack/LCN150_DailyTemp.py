def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            stacki, stackt = stack.pop()
            res[stacki] = i - stacki
        stack.append([i, t])
    return res

print(dailyTemperatures([30,38,30,36,35,40,28]))