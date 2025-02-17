from linkedlist import LinkedList, Node, printList

def getNthNodeFromEnd(head: Node, n):
    t = head
    stack = []
    
    while t is not None:
        stack.append(Node(t.data))
        t = t.next

    if n <= 1:
        return stack.pop()

    for i in range(n):
        out = stack.pop()

    return out

list = LinkedList([1, 2, 3, 4, 5])
o = getNthNodeFromEnd(list.head, 3)
print(o.data)