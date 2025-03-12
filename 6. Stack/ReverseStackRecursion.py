def insertAtBottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        temp = stack.pop()
        insertAtBottom(stack, item)
        stack.append(temp)

def reverse(stack):
    if stack:
        temp = stack.pop()
        reverse(stack)
        insertAtBottom(stack, temp)

# Example usage
if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5]
    print("Original Stack:", stack)
    reverse(stack)
    print("Reversed Stack:", stack)