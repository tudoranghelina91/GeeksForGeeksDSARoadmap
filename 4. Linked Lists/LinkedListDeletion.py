from linkedlist import Node, LinkedList, printList

def deleteAtBeginning(head: Node):
    t = head

    while t.next is not head:
        t = t.next

    t.next = head.next
    head = head.next

    return head

def deleteAtPosition(head: Node, pos = 0):
    if pos == 0:
        # Delete from beginning.... I know, dupes, but that's okay
        t = head

        while t.next is not head:
            t = t.next

        t.next = head.next
        head = head.next

        return head
    
    t = head
    prev = head
    cnt = 0
    
    while cnt != pos:
        prev = t
        t = t.next
        cnt += 1
    
    prev.next = t.next
    return head

def deleteAtEnd(head: Node):
    t = head
    
    while True:
        if t.next is None:
            break
        
        t = t.next
        
        if t.next.next is head:
            break

    t.next = head

    return head

list1 = LinkedList([1, 2, 3, 4, 5], True)
list2 = LinkedList([6, 7, 8, 9, 10], True)
list3 = LinkedList([1, 2, 3, 4, 5] ,True)

printList(deleteAtBeginning(list1.head))
printList(deleteAtPosition(list2.head, 3))
printList(deleteAtEnd(list3.head))