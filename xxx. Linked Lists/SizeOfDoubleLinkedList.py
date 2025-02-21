from doublelinkedlist import DoubleLinkedList, Node, printList

def sizeOfDoubleLinkedList(head: Node):
    if head is None:
        return 0
    
    t = head
    len = 0
    while t is not None:
        t = t.next
        len += 1
    
    return len
    
list = DoubleLinkedList([0, 2, 99])
printList(list.head)
print(sizeOfDoubleLinkedList(list.head))