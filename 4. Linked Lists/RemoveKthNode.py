from linkedlist import LinkedList, Node, printList


def deleteK(head: Node, k):
    #code here
    if head is None or k <= 0:
        return head
        
    curr = head
    prev = None
    
    count = 0
    
    while curr is not None:
        count += 1
        if count % k == 0:
            if prev is not None:
                prev.next = curr.next
            else:
                head = curr.next
        else:
            prev = curr
        
        curr = curr.next
        
    return head

list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
list = deleteK(list.head, 2)
printList(list)

