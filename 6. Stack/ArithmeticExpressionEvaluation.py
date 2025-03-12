def infixToPostfix(postfix):
    operatorStack = []
    output = []

    postfix = postfix.replace(" ", "")

    precedence = {'^': 2, '*': 1, '/': 1, '+': 0, '-': 0}

    for e in postfix:
        if e.isalnum():
            output.append(e)
        elif e == '(':
            operatorStack.append(e)
        elif e == ')':
            while operatorStack and operatorStack[-1] != '(':
                output.append(operatorStack.pop())
            operatorStack.pop()
        else:
            while operatorStack and operatorStack[-1] in precedence and precedence[operatorStack[-1]] >= precedence[e]:
                output.append(operatorStack.pop())
            operatorStack.append(e)
    
    while operatorStack:
        output.append(operatorStack.pop())

    return ''.join(output)

def arithmeticExpressionEvaluation(infix):
    postfix = infixToPostfix(infix)
    stack = []
    print(postfix)
    for e in postfix:
        if stack and e in ['^', '*', '/', '+', '-']:
            b = int(stack.pop())
            a = int(stack.pop())

            if e == '^':
                stack.append(a ** b)
            elif e == '*':
                stack.append(a * b)
            elif e == '/':
                stack.append(a // b)
            elif e == '+':
                stack.append(a + b)
            elif e == '-':
                stack.append(a - b)

        else:
            stack.append(e)
    
    return stack.pop()

print(arithmeticExpressionEvaluation("(2+4) * (4+6)"))