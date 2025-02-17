from linkedlist import LinkedList, Node

def getMiddle(head: Node):
    # since the fast pointer traverses the list twice as fast as the slow node
    # the slow node will always stop at the half of the list
    fast = head
    slow = head
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.data

list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])

print(getMiddle(list.head))