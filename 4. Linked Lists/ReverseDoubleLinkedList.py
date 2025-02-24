from linkedlist import Node

def reverseDoubleLinkedList(head: Node):
    if head is None or head.next is None:
        return head
    
    prev = None
    curr = head

    while curr is not None:
        prev = curr.prev
        curr.prev = curr.next
        curr.next = prev
        curr = curr.prev

    return prev.prev