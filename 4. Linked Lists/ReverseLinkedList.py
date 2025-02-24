from linkedlist import LinkedList, Node, printList

def reverseLinkedList(head: Node):
    # Initialize three pointers: curr, prev and next
    curr = head
    prev = None

    # Traverse all the nodes of Linked List
    while curr is not None:

        # Store next
        next = curr.next

        # Reverse current node's next pointer
        curr.next = prev

        # Move pointers one position ahead
        prev = curr
        curr = next

    # Return the head of reversed linked list
    return prev

list = LinkedList([1, 2, 3, 4, 5])
printList(reverseLinkedList(list.head))
