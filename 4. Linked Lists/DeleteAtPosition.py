from linkedlist import LinkedList, Node, printList


def deleteAtPosition(head: Node, position):
    t = head
    i = 0
    
    while i < position - 1:
        t = t.next
        i += 1

    temp = t
    t.next = t.next.next

    del(temp)
    return head

list = LinkedList([1,2,3,4,5])
printList(list.head)
list = deleteAtPosition(list.head, 1)
printList(list)