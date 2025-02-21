from linkedlist import LinkedList, Node, printList


def insertAtEnd(head,x):
    if head is None:
        head = Node(x)
        return head
        
    t = head
    while (t.next is not None):
        t = t.next
    
    t.next = Node(x)
        
    return head

list = LinkedList([1, 4, 5, 7])
list = insertAtEnd(list.head, 999)
printList(list)