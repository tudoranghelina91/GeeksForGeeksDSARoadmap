from linkedlist import LinkedList, Node, printList

def exchangeFirstLastNodeInCircular(head: Node):
    # Cases Handled: Linked List either empty or containing single node.
    if head == None or head.next == head:
        return head
    # Cases Handled: Linked List containing only two nodes
    elif head.next.next == head:
        head = head.next
        return head
    # Cases Handled: Linked List containing multiple nodes
    else:
        prev = None
        curr = head
        temp = head
        # finding last and second last nodes in linkedlist list
        while curr.next != head:
            prev = curr
            curr = curr.next
 
        # point the last node to second node of the list
        curr.next = temp.next
        # point the second last node to first node
        prev.next = temp
        # point the end of node to start ( make linked list circular )
        temp.next = curr
        # mark the starting of linked list
        head = curr
 
        return head
    
list = LinkedList([1,2,3,4,5], True)
printList(exchangeFirstLastNodeInCircular(list.head))