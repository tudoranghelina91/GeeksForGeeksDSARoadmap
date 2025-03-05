def prefixToPostfix(pre_exp):
    # Code here
    stack = []
    for i in range(len(pre_exp) - 1, -1, -1):
        if pre_exp[i] in ['*', '/', '+', '-']:
            stack.append(stack.pop() + stack.pop() + pre_exp[i])
        else:
            stack.append(pre_exp[i])
            
    return stack[0]

print(prefixToPostfix("*-A/BC-/AKL"))