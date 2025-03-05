
# The main idea is to use a stack to store the operands.
# Basically, whatever lies at the top of the stack is the new operand.
"""
Convert a prefix expression to an infix expression.
The function uses a stack to store operands and iterates through the prefix expression
from right to left. If an operand is encountered, it is pushed onto the stack. If an 
operator is encountered, two operands are popped from the stack, concatenated with the 
operator in the middle, and the result is pushed back onto the stack. This process 
continues until the end of the prefix expression is reached. The top of the stack 
contains the resulting infix expression.
Args:
    pre_exp (str): The prefix expression to be converted.
Returns:
    str: The resulting infix expression.
"""
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