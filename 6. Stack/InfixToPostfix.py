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