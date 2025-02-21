from linkedlist import LinkedList, Node, printList


def getNthNodeFromStart(head: Node, n):
    i = 0
    t = head
    if n < 0:
        return t
    
    while i < n:
        if t is None:
            return head
        
        t = t.next
        i += 1

    return Node(t.data)

list = LinkedList([1, 2, 3, 4, 5])
printList(getNthNodeFromStart(list.head, 3))