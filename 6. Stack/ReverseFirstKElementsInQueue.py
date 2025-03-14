def reverseFirstKElementsInQueue(queue, k):
    # [1, 2, 3, 4, 5] # [3, 2, 1, 4, 5]
    if k > len(queue):
        return None
    
    n = len(queue)

    stack = []
    second_queue = []
    output = []

    i = 0
    # 1. dequeue the first k elements and push them to a stack
    while i < k:
        stack.append(queue.pop(0))
        i += 1

    # 2. dequeue the remaining elements and push them to another queue
    while i < n:
        second_queue.append(queue.pop(0))
        i += 1

    # 3. push all the elements from the stack to the original queue
    while stack:
        output.append(stack.pop())

    # 4. push from the second queue back to the original queue\
    while second_queue:
        output.append(second_queue.pop(0))

    return output

inputq = [1, 2, 3, 4, 5]
print(reverseFirstKElementsInQueue(inputq, 3))