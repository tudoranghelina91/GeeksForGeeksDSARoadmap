# The idea is to use a stack. 
# We scan the input array from the start. 
# If it's an operand, we push it to the stack. 
# If it's an operator, we pop two operands from the stack, concatenate them with the operator and push the result back to the stack.

def postToPrefix(expression):
    stack = []
    for c in expression:
        if c in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            stack.append(c + a + b)
        else:
            stack.append(c)
            
    return stack.pop()

print(postToPrefix("ABC/-AK/L-*")) # *-A/BC-/AKL
# Time Complexity: O(n)