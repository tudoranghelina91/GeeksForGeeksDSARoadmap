"""
The idea is to use a stack and iterate the array in a forward only manner.
We will use a result array.

In the stack we store the (index, temp) pair at every step

When and while the current temp value is greater than the temp value on the stack we pop the index temperature pair out of the stack
We store the difference between the current index and the pair index in the output stack at the pair index position

(stackIndex, stackTemp) - pair to go on the stack
currentIndex - stackIndex - difference to store at output[stackIndex]

"""

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