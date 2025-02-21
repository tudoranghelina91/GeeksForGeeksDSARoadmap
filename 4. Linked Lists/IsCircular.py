from linkedlist import LinkedList, Node

def isCircular(head: Node):
    t = head
    while t.next is not None:
        t = t.next
        if t == head:
            return True
        
    return False

print(isCircular(LinkedList([1, 2, 3, 4, 5], True).head))

