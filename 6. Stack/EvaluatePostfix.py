def evaluate(arr):
    # code here
    stack = []
    for e in arr:
        if e in ['^', '*', '/', '+', '-']:
            b = int(stack.pop())
            a = int(stack.pop())
            
            if e == '^':
                stack.append(a ** b)
            elif e == '*':
                stack.append(a * b)
            elif e == '/':
                stack.append(int(a / b))
            elif e == '+':
                stack.append(a + b)
            elif e == '-':
                stack.append(a - b)
                
        else:
            stack.append(e)
            
    return stack.pop()

# Example usage
expression = ["2", "1", "+", "3", "*"]
result = evaluate(expression)
print(f"The result of the postfix expression {' '.join(expression)} is {result}")