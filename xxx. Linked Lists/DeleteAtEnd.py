from linkedlist import LinkedList, Node, printList

def deleteAtEnd(head: Node):
    t = head

    while t.next.next is not None:
        t = t.next

    aux = t.next
    t.next = None

    del aux

    return head

list = LinkedList([12, 3, 4, 5, 99, 8])
list = deleteAtEnd(list.head)
printList(list)
