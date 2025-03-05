"""
Convert an infix expression to a postfix expression using a stack.
The function uses a stack to store operators and a dictionary to store the precedence of operators.
It processes the input string character by character and applies the following rules:
1. If the character is an operand (alphanumeric), it is added to the output list.
2. If the character is an opening bracket '(', it is pushed onto the stack.
3. If the character is a closing bracket ')', operators are popped from the stack and added to the output list until an opening bracket '(' is encountered.
4. If the character is an operator, operators are popped from the stack and added to the output list until an operator with lower precedence is found or the stack is empty. The current operator is then pushed onto the stack.
After processing all characters, any remaining operators in the stack are added to the output list.
Args:
    s (str): The infix expression to be converted.
Returns:
    str: The resulting postfix expression.
"""
def infixToPostfix(s):
    st = []
    o = []
    p = {'^': 2, '*': 1, '/': 1, '+': 0, '-': 0 }

    for e in s:
        if e.isalnum():
            o.append(e)
        elif e == '(':
            st.append(e)
        elif e == ')':
            while st and st[-1] != '(':
                o.append(st.pop())
            st.pop()
        else:
            while st and st[-1] in p and p[st[-1]] >= p[e]:
                o.append(st.pop())
            st.append(e)
            
    while(st):
        o.append(st.pop())
            
    return ''.join(o)

print(infixToPostfix("a+b*(c^d-e)^(f+g*h)-i"))