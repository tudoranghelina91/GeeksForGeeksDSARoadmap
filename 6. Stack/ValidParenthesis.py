def isBalanced(s):
    # code here
    stack = []
    
    for c in s:
        if c == '{' or c == '[' or c == '(':
            stack.append(c)
            continue

        elif (c == '}' and stack and stack[-1] == '{') or \
        (c == ']' and stack and stack[-1] == '[') or \
        (c == ')' and stack and stack[-1] == '('):
            stack.pop()
            
        else:
            stack.append(c)

    if not stack:
        return True
        
    return False

# Example usage
if __name__ == "__main__":
    test_string = "{[()]}"
    print(isBalanced(test_string))
