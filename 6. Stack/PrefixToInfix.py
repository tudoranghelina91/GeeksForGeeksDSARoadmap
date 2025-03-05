
# The main idea is to use a stack to store the operands.
# We iterate through the prefix expression from right to left (reverse).
# If we encounter an operand, we push it to the stack.
# If we encounter an operator, we pop two operands from the stack and concatenate them with the operator in the middle.
# We then push the result back to the stack.
# We continue this process until we reach the end of the prefix expression.
# Basically, whatever lies at the top of the stack is the new operand.
# We return the top of the stack which contains the infix expression.
def prefixToInfix(pre_exp):
    stack = []
    
    for i in range(len(pre_exp) - 1, -1, -1):
        if pre_exp[i] in ['*', '/', '+', '-']:
            res = "(" + stack.pop() + pre_exp[i] + stack.pop() + ")"
            stack.append(res)
            
        else:
            stack.append(pre_exp[i])
                
    return stack.pop()

print(prefixToInfix("*-A/BC-/AKL"))