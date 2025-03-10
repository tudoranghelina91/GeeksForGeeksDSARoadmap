# 1. Convert from infix to postfix
def infixToPostfix(expression):
    stack = []
    output = []
    precedence = {'^': 2, '*': 1, '/': 1, '+': 0, '-': 0}

    for e in expression:
        if e.isalnum():
            output.append(e)
        elif e == '(':
            stack.append(e)
        elif e == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[e]:
                output.append(stack.pop())
            stack.append(e)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# 2. Convert from postfix to prefix
def postfixToPrefix(expression):
    stack = []
    for e in expression:
        if e not in ['^', '*', '/', '+', '-']:
            stack.append(e)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(e + a + b)

    return stack.pop()

def infixToPrefix(e):
    out = infixToPostfix(e)
    out = postfixToPrefix(out)

    return out

# Example usage
expression = "(a-b/c)*(a/k-l)"
print("Infix Expression: ", expression)
print("Infix TO Postfix Expression: ", infixToPostfix(expression))
print("Infix TO Prefix Expression: ", infixToPrefix(expression))