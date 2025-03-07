# The idea is to use a stack to store the operands and then pop them out when an operator is encountered.
# The operands are then concatenated with the operator in the middle to form the infix expression.
# We invert the order of the operands because the stack is LIFO.
def postToInfix(postfix):
    # Code here
    stack = []
    for c in postfix:
        if c in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            infix = '(' + a + c + b + ')'
            stack.append(infix)
        
        else:
            stack.append(c)
    
    return stack.pop()

# Example usage
if __name__ == "__main__":
    postfix = "ab*c+"
    print("Postfix expression:", postfix)
    print("Infix expression:", postToInfix(postfix))