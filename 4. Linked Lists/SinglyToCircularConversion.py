from linkedlist import LinkedList, Node, printList

def toCircular(head: Node):
    if head is None:
        return
    
    if head.next is None:
        head.next = head
        return

    t = head
    
    while t.next is not None:
        t = t.next

    t.next = head

list = LinkedList([1, 2, 3, 4, 5])
printList(list.head)
toCircular(list.head)
printList(list.head)